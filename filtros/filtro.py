import pandas as pd
import os
import subprocess
import logging
import re


def create_sigla(name):
    return ''.join([word[0] for word in name.split()]).upper()


def sanitize_path(path):
    """ Remove caracteres inválidos de um caminho de arquivo. """
    return re.sub(r'[<>:"/\\|?*]', '_', path)


def filter_and_save_excel(input_file, column_name, orgaos, update_progress):
    # Diretório de saída para relatórios
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_folder = os.path.join(desktop_path, 'Relatorios')
    os.makedirs(output_folder, exist_ok=True)

    # Caminho para o arquivo de log
    log_file_path = os.path.join(output_folder, 'log.txt')

    # Configuração do log
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

    try:
        update_progress("Lendo Planilha")
        logging.info("Lendo Planilha")
        df = pd.read_excel(input_file)

        update_progress("Organizando e Filtrando")
        logging.info("Organizando e Filtrando")

        for orgao in orgaos:
            update_progress(f"Filtrando dados para: {orgao}")
            filtered_df = df[df[column_name] == orgao]

            # Tratar a coluna 'DataFrequencia', convertendo para datetime
            if 'DataFrequencia' in filtered_df.columns:
                filtered_df['DataFrequencia'] = pd.to_datetime(
                    filtered_df['DataFrequencia'],
                    errors='coerce',  # Define 'NaT' para valores inválidos
                    dayfirst=True  # Especifica que o formato é dia/mês/ano
                )
                filtered_df['DataFrequencia'] = filtered_df['DataFrequencia'].dt.strftime('%d/%m/%Y')

            # Tratar colunas com formato de horas, se houver
            for col in filtered_df.columns:
                if 'Hora' in col or 'horário' in col.lower():  # Ajustar de acordo com os nomes das colunas
                    try:
                        filtered_df[col] = pd.to_datetime(filtered_df[col], format='%H:%M:%S', errors='coerce').dt.time
                    except Exception as e:
                        logging.warning(f"Falha ao formatar a coluna {col}: {e}")

            sigla = create_sigla(orgao)
            update_progress(f"Criando Arquivo para: {orgao}")
            logging.info(f"Criando Arquivo para: {orgao}")

            output_file = os.path.join(output_folder, f'{orgaos}.xlsx')
            filtered_df.to_excel(output_file, index=False)
            update_progress(f'Arquivo gerado: {output_file}')
            logging.info(f'Arquivo gerado: {output_file}')

        update_progress("Relatórios gerados com sucesso!")
        logging.info("Relatórios gerados com sucesso!")

    except Exception as e:
        error_message = f"Ocorreu um erro ao gerar os arquivos: {e}"
        update_progress(error_message)
        logging.error(error_message)

    # Abrir a pasta onde os arquivos foram salvos
    subprocess.Popen(f'explorer "{output_folder}"')

