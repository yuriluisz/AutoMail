import pandas as pd


def create_sigla(name):
    # Cria a sigla pegando a primeira letra de cada palavra no nome ( NÃO USADA )
    return ''.join([word[0] for word in name.split()]).upper()


def filter_and_save_excel(input_file, column_name, orgaos):
    # Ler a planilha
    print("Lendo Planilha")
    df = pd.read_excel(input_file)

    try:
        print("Organizando e Filtrando")
        for orgao in orgaos:
            filtered_df = df[df[column_name] == orgao]

            # Corrigir formatação da coluna "DataFrequencia"
            if 'DataFrequencia' in filtered_df.columns:
                filtered_df['DataFrequencia'] = pd.to_datetime(filtered_df['DataFrequencia'],
                                                               errors='coerce').dt.strftime('%d/%m/%Y')

            sigla = create_sigla(orgao)
            print(f"Criando Arquivo, Aguarde")
            output_file = f'Diretorio/de/saida/dos/arquivos/{orgao}.xlsx'
            filtered_df.to_excel(output_file, index=False)
            print(f'Arquivo gerado: {output_file}')
    except Exception as e:
        print(f"Ocorreu ao gerar o arquivo: {e}")

    print("Relatorios gerados com sucesso!")


# Orgãos dentro da coluna orgão a serem filtrados em ordem de relatorio geral
input_file = input("Insira o Caminho do Arquivo: ")
column_name = 'ORGAO'
orgaos = [
]

filter_and_save_excel(input_file, column_name, orgaos)
