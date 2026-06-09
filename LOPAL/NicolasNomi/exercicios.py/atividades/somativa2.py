# # 1.Registro de operador
# import tkinter as tk
# from tkinter import messagebox

# #.get() serve para buscar informação na caixa de texto
# def janela_bemvindo():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()


#     if nome == "" and turno == "":
#         messagebox.showwarning("Aviso", "Digite seu nome e seu turno :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá Operador {nome} registrado no Turno {turno}. Boa jornada!")

# # JANELA
# janela = tk.Tk()
# janela.title("REGISTRO OPERADOR")
# janela.geometry("400x200")
# janela.configure(bg="pink")



# #COMPONENTES
# #botton = lbl_
# lbl_texto = tk.Label(janela, text= "Digite seu Nome:  ")
# lbl_texto.grid(row=0, column=0, pady=10, padx=10)
# lbl_idade = tk.Label(janela, text= "Digite seu Turno:   ")
# lbl_idade.grid(row=1, column=0, pady=10, padx=10)

# # A dimensao/posição da janela
# # lbl_texto.pack (pady=10)
# # lbl_texto.pack (padx=10)

# nome_usuario = tk.Entry (janela, font= ("Arial 12", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# turno_usuario = tk.Entry (janela, font= ("Arial 12", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)



# # FUNCIONAR JANELA
# janela.mainloop()

# 2. Calculo de prooduçao

# import tkinter as tk
# from tkinter import messagebox

# #.get() serve para buscar informação na caixa de texto
# def janela_bemvindo():
#     peças = int(peças_usuario.get())
#     resultado = peças * 8

#     if peças == "" :
#         messagebox.showwarning("Aviso", "Digite as peças :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Você terá {resultado} de peças produzidas em oito horas.")

# # JANELA
# janela = tk.Tk()
# janela.title("PEÇAS")
# janela.geometry("800x600")
# janela.configure(bg="pink")



# #COMPONENTES
# #botton = lbl_
# lbl_peças = tk.Label(janela, text= "Peças produzidas em uma hora")
# lbl_peças.grid(row=0, column=0, pady=50, padx=50)

# # A dimensao/posição da janela
# # lbl_texto.pack (pady=10)
# # lbl_texto.pack (padx=10)

# peças_usuario = tk.Entry (janela, font= ("Arial 12", 12))
# peças_usuario.grid(row=0, column=1, pady=50, padx=50)

# btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=50, padx=50)


# # FUNCIONAR JANELA
# janela.mainloop()

# 3.Conversor de Unidade

# import tkinter as tk
# from tkinter import messagebox

# def converter_pressao():
#     valor_convertendo = bar.get()
    
#     if valor_convertendo == "":
#         messagebox.showwarning("Aviso", "Por favor, digite um valor em Bar")

#     else:
#         valor_bar = int(valor_convertendo)
        
#         convertendo = valor_bar * 14.5
        
#         messagebox.showinfo("Resultado", f"O valor de {valor_bar} bar equivale a {convertendo:.2f} psi.")
        


# janela = tk.Tk()
# janela.title("Conversor de Pressão")
# janela.geometry("800x600")
# janela.configure(bg="pink")

# lbl_texto = tk.Label(janela, text="Digite a pressão em Bar", font=("Arial", 12), bg="pink")
# lbl_texto.grid(row=0, column=0, pady=50, padx=20)

# bar = tk.Entry(janela, font=("Arial", 12))
# bar.grid(row=0, column=1, pady=50, padx=20)

# btn_mensagem = tk.Button(janela, text="Converter para psi", font=("Arial", 11), command=converter_pressao)
# btn_mensagem.grid(row=1, column=0, pady=20, padx=20)

# janela.mainloop()

# 4. Média de qualidade

# import tkinter as tk
# from tkinter import messagebox

# def calcular_media():
#         media = notas / 3
#         n1 = int(entry_nota1.get())
#         n2 = int(entry_nota2.get())
#         n3 = int(entry_nota3.get())
       
#         if calcular_media():
#             messagebox.showwarning("Aviso", "Por favor, digite notas entre 0 e 10.")

#         else:
#               messagebox.showinfo("Total", f"A sua média foi de {media}!")

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("800x600") 
# janela.configure(bg="pink")

# lbl_nota1 = tk.Label(janela, text="Primeira Nota:", bg="black", fg="white", width=12)
# lbl_nota1.grid(row=0, column=0, pady=10, padx=10)
# entry_nota1 = tk.Entry(janela, font=("Arial", 12))
# entry_nota1.grid(row=0, column=1, pady=10, padx=10)

# lbl_nota2 = tk.Label(janela, text="Segunda Nota:", bg="black", fg="white", width=12)
# lbl_nota2.grid(row=1, column=0, pady=10, padx=10)
# entry_nota2 = tk.Entry(janela, font=("Arial", 12))
# entry_nota2.grid(row=1, column=1, pady=10, padx=10)

# lbl_nota3 = tk.Label(janela, text="Terceira Nota:", bg="black", fg="white", width=12)
# lbl_nota3.grid(row=2, column=0, pady=10, padx=10)
# entry_nota3 = tk.Entry(janela, font=("Arial", 12))
# entry_nota3.grid(row=2, column=1, pady=10, padx=10)

# btn_calcular = tk.Button(janela, text="Calcular Média", font=("Arial", 11), command=calcular_media)
# btn_calcular.grid(row=3, column=0, columnspan=2, pady=20)

# janela.mainloop()

# 5. Termostato Inteligente

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     baixa_carga = int(um.get())
#     normal = int(dois.get())
#     ALERTA_Resfriamento_automatico = int(tres.get())

# janela = tk.Tk()
# janela.title("TERMOSTATO INTELIGENTE")
# janela.geometry("800x600")
# janela.configure(bg="pink")

# lbl_texto = tk.Label(janela, text="Qual temperatura está?", bg="black", fg="white", width=12)
# lbl_texto.grid(row=0, column=1, pady=10, padx=10)