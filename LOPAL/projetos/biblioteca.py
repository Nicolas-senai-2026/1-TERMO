# =====================================================================
#          SISTEMA DE GESTÃO DE BIBLIOTECA (VERSÃO 1.0 CORRIGIDA)
# =====================================================================

import tkinter as tk
from tkinter import messagebox

# --- FUNÇÕES DE INTERAÇÃO ---

def janela_bemvindo():
    aluno = aluno_usuario.get()
    comunidade = comunidade_usuario.get()

    if aluno == "" or comunidade == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos da tela principal. :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {aluno} ({comunidade}) - Seja bem-vindo ao nosso sistema")


def abrir_segunda_janela():
    janela_livros = tk.Toplevel(janela)
    janela_livros.title("LIVROS")
    janela_livros.geometry("450x200")
    janela_livros.configure(bg="black")

    lbl_livro = tk.Label(janela_livros, text="Você deseja livro básico ou raro:", bg="black", fg="white")
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


def abrir_janela_taxa():
    # Transformamos a antiga 'janela3' em uma janela Toplevel controlada por esta função
    janela3 = tk.Toplevel(janela)
    janela3.title("TAXA DE RENOVAÇÃO")
    janela3.geometry("500x200")
    janela3.configure(bg="black")

    lbl_taxa = tk.Label(janela3, text="Digite quanto tempo quer ficar com o livro:", bg="black", fg="white")
    lbl_taxa.grid(row=0, column=0, pady=10, padx=10)

    tempo_livro = tk.Entry(janela3, font=("Arial", 12))
    tempo_livro.grid(row=0, column=1, pady=10, padx=10)

    def taxa_renovacao():
        taxa = tempo_livro.get()
        if taxa == "":
            messagebox.showwarning("Aviso", "Quanto tempo você quer ficar com o livro?")
        else:
            messagebox.showinfo("Informação", f"Período de {taxa} dias registrado. A cada dia extra você terá que pagar R$5,00 de taxa.")

    btn_tempo = tk.Button(janela3, text="Confirmar Tempo", command=taxa_renovacao)
    btn_tempo.grid(row=1, column=0, columnspan=2, pady=10)


# --- JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("BIBLIOTECA COMUNITÁRIA")
janela.geometry("450x300")
janela.configure(bg="black")

# Labels (Adicionado bg e fg para os textos aparecerem no fundo preto)
lbl_mensagem = tk.Label(janela, text="Digite seu Nome:", bg="black", fg="white")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10, sticky="w")

lbl_idade = tk.Label(janela, text="Aluno ou Comunidade:", bg="black", fg="white")
lbl_idade.grid(row=1, column=0, pady=10, padx=10, sticky="w")

# Entries
aluno_usuario = tk.Entry(janela, font=("Arial", 12))
aluno_usuario.grid(row=0, column=1, pady=10, padx=10)

comunidade_usuario = tk.Entry(janela, font=("Arial", 12))
comunidade_usuario.grid(row=1, column=1, pady=10, padx=10)

# Botões de Navegação e Ações
btn_mensagem = tk.Button(janela, text="Boas-vindas", command=janela_bemvindo, width=15)
btn_mensagem.grid(row=2, column=0, columnspan=2, pady=5)

btn_segunda_janela = tk.Button(janela, text="Selecionar Livros", command=abrir_segunda_janela, width=15)
btn_segunda_janela.grid(row=3, column=0, columnspan=2, pady=5)

btn_terceira_janela = tk.Button(janela, text="Verificar Taxas", command=abrir_janela_taxa, width=15)
btn_terceira_janela.grid(row=4, column=0, columnspan=2, pady=5)

# Iniciar o loop do sistema
janela.mainloop()