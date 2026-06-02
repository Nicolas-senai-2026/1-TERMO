import tkinter as tk
from tkinter import messagebox

#.get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()
    idade = idade_usuario.get()


    if nome == "" and idade == "":
        messagebox.showwarning("Aviso", "Digite seu nome e sua idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome} e {idade} - Seja bem-vindo ao nosso sistema")

# JANELA
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("400x200")
janela.configure(bg="pink")



#COMPONENTES
#botton = lbl_
lbl_texto = tk.Label(janela, text= "Digite seu Nome:  ")
lbl_texto.grid(row=0, column=0, pady=10, padx=10)
lbl_idade = tk.Label(janela, text= "Digite sua Idade:   ")
lbl_idade.grid(row=1, column=0, pady=10, padx=10)

# A dimensao/posição da janela
# lbl_texto.pack (pady=10)
# lbl_texto.pack (padx=10)

nome_usuario = tk.Entry (janela, font= ("Arial 12", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)
idade_usuario = tk.Entry (janela, font= ("Arial 12", 12))
idade_usuario.grid(row=1, column=1, pady=10, padx=10)


btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)



# FUNCIONAR JANELA
janela.mainloop()