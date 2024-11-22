import tkinter as tk
from tkinter import filedialog, messagebox
from filtro import filter_and_save_excel
import os
import logging
import pandas as pd

# Variável global para armazenar o caminho do arquivo
selected_file_path = ""
log_file_path = ""


def select_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(title="Selecione o arquivo que deseja:")
    if file_path:
        selected_file_path = file_path
        label_file_path.config(text=file_path, fg="darkgreen")


def start_filtering():
    if selected_file_path:
        column_name = 'ORGAO'
        orgaos = [

        ]

        # Configuração do arquivo de log
        log_dir = os.path.dirname(selected_file_path)
        global log_file_path
        log_file_path = os.path.join(log_dir, 'log.txt')

        # Inicializar logging
        logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info("Início da filtragem.")

        text_progress.config(state=tk.NORMAL)
        text_progress.delete(1.0, tk.END)
        text_progress.insert(tk.END, "Iniciando a filtragem...\n")
        text_progress.config(state=tk.DISABLED)

        # Função de callback para atualizar a interface com o progresso
        def update_progress(message):
            text_progress.config(state=tk.NORMAL)
            text_progress.insert(tk.END, message + "\n")
            text_progress.config(state=tk.DISABLED)
            text_progress.yview(tk.END)
            logging.info(message)

        # Filtrar e salvar dados
        filter_and_save_excel(selected_file_path, column_name, orgaos, update_progress)

        # Finalizar
        text_progress.config(state=tk.NORMAL)
        text_progress.insert(tk.END, "Filtragem concluída!\n")
        text_progress.config(state=tk.DISABLED)
        logging.info("Filtragem concluída.")

        messagebox.showinfo("Concluído", "A filtragem foi concluída com sucesso!")


def quit_app():
    root.destroy()


# Função de filtragem com tratamento de horas
def filter_and_save_excel(file_path, column_name, orgaos, update_progress):
    # Carregar o arquivo Excel
    if file_path.endswith('.xlsb'):
        df = pd.read_excel(file_path, engine='pyxlsb')
    else:
        df = pd.read_excel(file_path)

    # Filtrar os dados baseados na coluna e nos órgãos especificados
    filtered_df = df[df[column_name].isin(orgaos)]

    # Salvar o arquivo filtrado (converter para xlsx)
    output_file_path = file_path.replace(".xlsb", "_filtrado.xlsx").replace(".xlsx", "_filtrado.xlsx")
    filtered_df.to_excel(output_file_path, index=False)

    update_progress(f"Arquivo salvo em: {output_file_path}")


# Criação da janela principal
root = tk.Tk()
root.title("Filtragem de Dados Excel")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#dedede")

# Frame superior (75% da tela)
frame_top = tk.Frame(root, bg="#dedede")
frame_top.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.75, anchor='n')

# Frame inferior (25% da tela)
frame_bottom = tk.Frame(root, bg="#dedede")
frame_bottom.place(relx=0.5, rely=0.85, relwidth=0.9, relheight=0.15, anchor='s')

# Texto e label para exibir o caminho do arquivo no frame superior
label_instruction = tk.Label(frame_top, text="Insira o local do arquivo:", bg="#dedede", font=("Arial", 16))
label_instruction.pack(pady=20)

label_file_path = tk.Label(frame_top, text="", bg="#dedede", font=("Arial", 14))
label_file_path.pack(pady=10)

button_browse = tk.Button(frame_top, text="Selecionar Arquivo", command=select_file, font=("Arial", 14), width=20,
                          height=2)
button_browse.pack(pady=10)

# Área de texto para exibir o progresso da filtragem
text_progress = tk.Text(frame_top, state=tk.DISABLED, wrap='word', font=("Arial", 12))
text_progress.pack(pady=20, fill=tk.BOTH, expand=True)

# Botões no frame inferior
button_start = tk.Button(frame_bottom, text="Iniciar Filtragem", command=start_filtering, font=("Arial", 14), width=20,
                         height=2)
button_start.pack(side=tk.LEFT, padx=20)

button_exit = tk.Button(frame_bottom, text="Sair", command=quit_app, font=("Arial", 14), width=20, height=2)
button_exit.pack(side=tk.RIGHT, padx=20)

root.mainloop()
