import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import area
import contagem
import tirarfundo

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entrada_pasta.delete(0, tk.END)
    entrada_pasta.insert(0, pasta)

def selecionar_diretorioXLSX():
    diretorio = filedialog.askdirectory(title='Selecionar o Diretório para Salvar os Dados')
    entrada_dir.delete(0, tk.END)
    entrada_dir.insert(0, diretorio)

def salvarXLSX(dados):
    localXLSX = entrada_dir.get()
    nomeXLSX = entrada_nomeXSLX.get()

    if not localXLSX or not nomeXLSX:
        tk.messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    pathXLSX = f'{localXLSX}\{nomeXLSX}.xlsx'
    # Salvar dados em um arquivo Excel
    df = pd.DataFrame(dados)
    df.to_excel(pathXLSX, index=False)

def limpar_dados():
    entrada_pasta.delete(0, tk.END)
    entrada_dir.delete(0, tk.END)
    entrada_nomeXSLX.delete(0, tk.END)
    var_salvar_fotos.set(False)  # Desmarcar a opção de salvar fotos
    progress["value"] = 0  # Resetar a barra de progresso
    messagebox.showinfo("Limpeza", "Todos os campos foram limpos!")

def iniciar_processamento():
    pasta = entrada_pasta.get()
    local_xlsx = entrada_dir.get()
    salvar_fotos = var_salvar_fotos.get()

    if not pasta or not local_xlsx:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    try:
        arquivos = os.listdir(pasta)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Diretório inválido.")
        return

    arquivos_validos = [file for file in arquivos if os.path.splitext(file)[1].lower() in {".png", ".jpg", ".jpeg", ".tif"}]
    narquivos = len(arquivos_validos)

    if narquivos == 0:
        messagebox.showwarning("Aviso", "Nenhum arquivo válido encontrado na pasta.")
        return

    dados = []
    progress["maximum"] = narquivos
    nfotos = 1

    for index, file in enumerate(arquivos_validos, start=1):
        caminho = os.path.join(pasta, file)

        # Exemplo de chamadas às funções do programa
        pixel_count = area.calc_area(caminho)
        azul, marrom = contagem.n_pontos(caminho, salvar_fotos, nfotos)

        dados.append({
            "Index": index,
            "Nome do Arquivo": file,
            "Área": pixel_count,
            "Biomarcadores Azuis": azul,
            "Biomarcadores Marrons": marrom
        })

        # Atualizar progresso
        progress["value"] = index
        janela.update_idletasks()
        nfotos += 1

    salvarXLSX(dados)

    messagebox.showinfo("Sucesso", "Processamento concluído e dados salvos!")
    limpar_dados()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Processador de Imagens")
janela.geometry("500x400")

# Entrada do diretório da pasta
tk.Label(janela, text="Diretório da pasta:").pack(pady=5)
frame_pasta = tk.Frame(janela)
frame_pasta.pack()
entrada_pasta = tk.Entry(frame_pasta, width=40)
entrada_pasta.pack(side=tk.LEFT, padx=5)
btn_pasta = tk.Button(frame_pasta, text="Selecionar", command=selecionar_pasta)
btn_pasta.pack(side=tk.RIGHT)

# Entrada para salvar o arquivo Excel
tk.Label(janela, text="Diretório para Salvar o arquivo XLSX:").pack(pady=5)
frame_xlsx = tk.Frame(janela)
frame_xlsx.pack()
entrada_dir = tk.Entry(frame_xlsx, width=40)
entrada_dir.pack(side=tk.LEFT, padx=5)
btn_xlsx = tk.Button(frame_xlsx, text="Selecionar", command=selecionar_diretorioXLSX)
btn_xlsx.pack(side=tk.RIGHT)

# Nome arquivo XLSX
tk.Label(janela, text="Nome do arquivo (sem extensão):").pack()
entrada_nomeXSLX = tk.Entry(janela, width=50)
entrada_nomeXSLX.pack()

# Opção para salvar fotos
var_salvar_fotos = tk.BooleanVar()
chk_salvar_fotos = tk.Checkbutton(janela, text="Salvar Fotos Processadas", variable=var_salvar_fotos)
chk_salvar_fotos.pack(pady=5)

# Botão para iniciar processamento
btn_iniciar = tk.Button(janela, text="Iniciar Processamento", command=iniciar_processamento)
btn_iniciar.pack(pady=10)

# Barra de progresso
tk.Label(janela, text="Progresso:").pack(pady=5)
progress = Progressbar(janela, orient=tk.HORIZONTAL, length=300, mode="determinate")
progress.pack(pady=5)

# Limpar todas as opções
btn_limpar = tk.Button(janela, text="Limpar Tudo", command=limpar_dados)
btn_limpar.pack(pady=10)

# Rodar a interface
janela.mainloop()
