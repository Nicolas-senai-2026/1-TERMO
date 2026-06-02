# =====================================================================
#             SISTEMA DE GESTÃO DE BIBLIOTECA (VERSÃO 1.0)
# =====================================================================

import tkinter as tk
from tkinter import messagebox

print("\n=========================================")
print("          BIBLIOTECA COMUNITÁRIA         ")
print("=========================================")
print("1. Registrar Novo Empréstimo")
print("2. Ver Relatório e Fechar Sistema")
print("=========================================")


def janela_bemvindo():
    aluno = aluno_usuario.get()
    comunidade = comunidade_usuario.get()

    if aluno == "" and comunidade == "":
        messagebox.showwarning("Aviso", "Digite seu nome e sua idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {aluno} e {comunidade} - Seja bem-vindo ao nosso sistema")



def abrir_segunda_janela():
    
    janela_livros = tk.Toplevel(janela)
    janela_livros.title("LIVROS")
    janela_livros.geometry("550x550")
    janela_livros.configure(bg="black")

    
    lbl_livro = tk.Label(janela_livros, text="Você deseja livro básico ou raro:  ")
    lbl_livro.grid(row=0, column=0, pady=10, padx=10)

    livro_usuario = tk.Entry(janela_livros, font=("Arial", 12))
    livro_usuario.grid(row=0, column=1, pady=10, padx=10)
    
    
    def checar_livro():
        livro = livro_usuario.get()
        if livro == "":
            messagebox.showwarning("Aviso", "Você quer livro básico ou raro?")
        else:
            messagebox.showinfo("Sucesso", f"Livro '{livro}' selecionado!")

   
    btn_checar = tk.Button(janela_livros, text="Confirmar Livro", command=checar_livro)
    btn_checar.grid(row=1, column=0, columnspan=2, pady=10)

def taxa_renovaçao():
    taxa = tempo_livro.get()
    if taxa == "":
        messagebox.showwarning("Aviso", "Quanto tempo você quer ficar com o livro?")
    else:
        messagebox.showinfo("Ok, a cada dia extra você terá que pagar R$5,00 de taxa")

janela3 = tk.Tk()
janela3.title("TAXA DE RENOVAÇÃO")
janela3.geometry("550x550")
janela3.configure(bg="black")

lbl_taxa = tk.Label(taxa_renovaçao, text="Digite quanto tempo você quer ficar com livro:  ")
lbl_taxa.grid(row=0, column=0, pady=10, padx=10)

tempo_livro = tk.Entry(taxa_renovaçao, font=("Arial", 12))
tempo_livro.grid(row=0, column=1, pady=10, padx=10)

btn_tempo = tk.Button(taxa_renovaçao, text="Mensagem", command=janela_bemvindo)
btn_tempo.grid(row=2, column=0, pady=10, padx=10)

janela = tk.Tk()
janela.title("BIBLIOTECA COMUNITÁRIA")
janela.geometry("550x550")
janela.configure(bg="black")

# lbl_
lbl_mensagem = tk.Label(janela, text="Digite seu Nome:  ")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

lbl_idade = tk.Label(janela, text="Aluno ou Comunidade:   ")
lbl_idade.grid(row=1, column=0, pady=10, padx=10)

# Entrys
aluno_usuario = tk.Entry(janela, font=("Arial", 12))
aluno_usuario.grid(row=0, column=1, pady=10, padx=10)

comunidade_usuario = tk.Entry(janela, font=("Arial", 12))
comunidade_usuario.grid(row=1, column=1, pady=10, padx=10)

# Botões
btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


btn_segunda_janela = tk.Button(janela, text="Abrir Biblioteca", command=abrir_segunda_janela)
btn_segunda_janela.grid(row=3, column=0, pady=10, padx=10)


#funcionar tudo
janela.mainloop()