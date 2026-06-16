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
#         messagebox.showinfo("Bem-Vindo", f"Operador {nome} registrado no Turno {turno}. Boa jornada!")

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
#     try:

#         n1 = float(entry_nota1.get())
#         n2 = float(entry_nota2.get())
#         n3 = float(entry_nota3.get())
        
#         if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10):
#             messagebox.showwarning("Aviso", "Por favor, digite notas entre 0 e 10.")

#         media = (n1 + n2 + n3) / 3
        
        
#         messagebox.showinfo("Total", f"A sua média foi de {media:.2f}!")
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("800x600") 
# janela.configure(bg="pink")

# lbl_notas1 = tk.Label(janela, text="Primeira Nota:", bg="black", fg="white", width=12)
# lbl_notas1.grid(row=0, column=0, pady=10, padx=10)
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

# def verificar_temperatura():
#     temp = float(entry_temp.get())

#     if temp < 40:
#         messagebox.showinfo("Status", "Baixa carga")
#     elif temp <= 70:
#         messagebox.showinfo("Status", "Normal")
#     else:
#         messagebox.showwarning("Status", "ALERTA: Resfriamento Ativado!")

# janela = tk.Tk()
# janela.title("Termostato")
# janela.geometry("800x600")
# janela.configure(bg="pink")

# lbl = tk.Label(janela, text="Digite a temperatura:")
# lbl.pack(pady=5)

# entry_temp = tk.Entry(janela)
# entry_temp.pack(pady=5)

# btn = tk.Button(janela, text="Verificar", command=verificar_temperatura)
# btn.pack(pady=10)

# janela.mainloop()

# 6.Classificador de Lotes

# import tkinter as tk
# from tkinter import messagebox

# def verificar_produto():
#     codigo = entry_codigo.get()

#     if codigo[0] == "A":
#         messagebox.showinfo("Categoria", "Alimentos")
#     elif codigo[0] == "E":
#         messagebox.showinfo("Categoria", "Eletrônicos")
#     else:
#         messagebox.showinfo("Categoria", "Desconhecido")

# janela = tk.Tk()
# janela.title("Categorias")
# janela.geometry("800x600")
# janela.configure(bg="pink")

# lbl = tk.Label(janela, text="Digite o código do produto:")
# lbl.pack(pady=5)

# entry_codigo = tk.Entry(janela)
# entry_codigo.pack(pady=5)

# btn = tk.Button(janela, text="Verificar Categoria", command=verificar_produto)
# btn.pack(pady=10)

# janela.mainloop()

# 7.Segurança de Operação

# import tkinter as tk
# from tkinter import messagebox

# def sensor_botao():
#     codigo = entry_sensor.get()
#     if codigo == "sim":
#         messagebox.showwarning("Como está o sensor da porta? Aberto ou fechada:")

#     else:
#         messagebox.showinfo("A sua maquina está pronta para iniciar!")


# janela = tk.Tk()
# janela.title("Segurança de Operaçãos")
# janela.geometry("800x600")
# janela.config(bg="pink")

# lbl = tk.Label(janela, text="Sensor da porta está fechada? Botão de emergência está desligado?:")
# lbl.pack(pady=5)

# entry_sensor = tk.Entry(janela)
# entry_sensor.pack(pady=5)

# btn = tk.Button(janela, text="Verificar Segurança", command=sensor_botao)
# btn.pack(pady=10)

# janela.mainloop()

# 8.Cálculo de Descarte

import tkinter as tk
from tkinter import messagebox



# 11.Soma de Produção (Acumulador):

# import tkinter as tk
# from tkinter import messagebox

# def criar_app_acumulador():
#     total_peso = [0.0]

#     def adicionar_peso(event=None):
#         try:
#             peso = float(entry_peso.get())
            
#             if peso == 0:
#                 finalizar_producao()
#             elif peso < 0:
#                 messagebox.showwarning("Aviso", "Por favor, insira um peso maior que zero.")
#                 entry_peso.delete(0, tk.END)
#             else:
#                 total_peso[0] += peso
#                 # Atualiza a lista visual de caixas adicionadas
#                 lista_caixas.insert(tk.END, f"Caixa: {peso:.2f} kg")
#                 # Limpa o campo de texto para a próxima digitação
#                 entry_peso.delete(0, tk.END)
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite um número válido.")
#             entry_peso.delete(0, tk.END)

#     def finalizar_producao():
#         # Mostra o resultado final em um popup
#         messagebox.showinfo("Produção Encerrada", f"O peso total acumulado é:\n\n{total_peso[0]:.2f} kg")
#         # Zera o acumulador e limpa a tela para uma nova pesagem
#         total_peso[0] = 0.0
#         lista_caixas.delete(0, tk.END)
#         entry_peso.delete(0, tk.END)

#     # --- Configuração da Janela Principal ---
#     janela = tk.Tk()
#     janela.title("Controle de Produção")
#     janela.geometry("350x400")
#     janela.resizable(False, False)

#     # Componentes Visuais (Widgets)
#     lbl_instrucao = tk.Label(janela, text="Digite o peso da caixa (kg):", font=("Arial", 11, "bold"))
#     lbl_instrucao.pack(pady=10)

#     entry_peso = tk.Entry(janela, font=("Arial", 12), justify="center")
#     entry_peso.pack(pady=5)
#     entry_peso.focus()  # Coloca o cursor automaticamente no campo de texto
#     # Permite pressionar "Enter" no teclado para adicionar
#     entry_peso.bind("<Return>", adicionar_peso) 

#     btn_adicionar = tk.Button(janela, text="Adicionar Caixa", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=adicionar_peso)
#     btn_adicionar.pack(pady=5)

#     lbl_historico = tk.Label(janela, text="Caixas na esteira atual:", font=("Arial", 9, "italic"))
#     lbl_historico.pack(pady=5)

#     # Lista para o usuário ver o que já adicionou
#     lista_caixas = tk.Listbox(janela, font=("Arial", 10), width=30, height=8)
#     lista_caixas.pack(pady=5)

#     btn_finalizar = tk.Button(janela, text="Finalizar e Somar (ou digite 0)", bg="#F44336", fg="white", font=("Arial", 10, "bold"), command=finalizar_producao)
#     btn_finalizar.pack(pady=15)

#     janela.mainloop()

# 12.Múltiplas Leituras:

# import tkinter as tk
# from tkinter import messagebox

# # Variáveis para guardar os dados
# leituras = []

# def registrar():
#     try:
#         # Pega a temperatura digitada
#         temp = float(entry_temp.get())
#         leituras.append(temp)
        
#         # Limpa o campo de texto
#         entry_temp.delete(0, tk.END)
        
#         # Se já leu 5 vezes, mostra o resultado e fecha a janela
#         if len(leituras) == 5:
#             maior = max(leituras)
#             messagebox.showinfo("Resultado", f"A maior temperatura foi: {maior}°C")
#             janela.destroy() # Fecha o programa
            
#     except ValueError:
#         messagebox.showerror("Erro", "Digite um número válido!")

# # --- Configuração da Janela ---
# janela = tk.Tk()
# janela.title("Sensores")
# janela.geometry("250x150")

# # Componentes da tela
# lbl = tk.Label(janela, text="Digite a temperatura:")
# lbl.pack(pady=10)

# entry_temp = tk.Entry(janela)
# entry_temp.pack(pady=5)

# btn = tk.Button(janela, text="Enviar", command=registrar)
# btn.pack(pady=10)

# janela.mainloop()

# 13.Painel de Login:

# import tkinter as tk
# from tkinter import messagebox

# # Variável para controlar as tentativas restantes
# tentativas = [3]

# def verificar_login():
#     senha_correta = "admin123"
#     senha_digitada = entry_senha.get()
    
#     if senha_digitada == senha_correta:
#         messagebox.showinfo("Sucesso", "Acesso Permitido!")
#         janela.destroy() # Fecha o programa
#     else:
#         tentativas[0] -= 1 # Reduz uma tentativa
#         entry_senha.delete(0, tk.END) # Limpa o campo
        
#         if tentativas[0] > 0:
#             messagebox.showwarning("Erro", f"Acesso Negado!\nTentativas restantes: {tentativas[0]}")
#         else:
#             messagebox.showerror("Bloqueado", "Painel Bloqueado!")
#             janela.destroy() # Fecha o programa pois bloqueou

# # --- Configuração da Janela ---
# janela = tk.Tk()
# janela.title("Login")
# janela.geometry("250x150")

# # Componentes da tela
# lbl = tk.Label(janela, text="Digite a senha do supervisor:")
# lbl.pack(pady=10)

# # O argumento show="*" esconde os caracteres da senha na tela
# entry_senha = tk.Entry(janela, show="*")
# entry_senha.pack(pady=5)

# btn = tk.Button(janela, text="Entrar", command=verificar_login)
# btn.pack(pady=10)

# janela.mainloop()

# 14.Simulador de Estoque:

# import tkinter as tk
# from tkinter import messagebox

# # Estoque inicial guardado em uma lista para podermos alterar dentro da função
# estoque = [100]

# def atualizar_estoque(operacao):
#     try:
#         qtd = int(entry_qtd.get())
        
#         if qtd <= 0:
#             messagebox.showwarning("Aviso", "Digite um valor maior que zero.")
#             return

#         if operacao == "add":
#             estoque[0] += qtd
#         elif operacao == "rem":
#             if qtd > estoque[0]:
#                 messagebox.showerror("Erro", "Quantidade indisponível em estoque!")
#                 return
#             estoque[0] -= qtd
            
#         # Atualiza o texto na tela
#         lbl_total.config(text=f"Estoque Atual: {estoque[0]}")
#         entry_qtd.delete(0, tk.END) # Limpa o campo
        
#         # Verifica se o estoque está crítico
#         if estoque[0] < 10:
#             messagebox.showwarning("Alerta", "Estoque Crítico!")
            
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite um número inteiro válido.")

# # --- Configuração da Janela ---
# janela = tk.Tk()
# janela.title("Controle de Estoque")
# janela.geometry("250x220")

# # Componentes da tela
# lbl_total = tk.Label(janela, text=f"Estoque Atual: {estoque[0]}", font=("Arial", 12, "bold"))
# lbl_total.pack(pady=15)

# lbl_qtd = tk.Label(janela, text="Quantidade:")
# lbl_qtd.pack()

# entry_qtd = tk.Entry(janela, justify="center")
# entry_qtd.pack(pady=5)

# # Botões de ação
# btn_add = tk.Button(janela, text="Adicionar Itens", bg="#4CAF50", fg="white", width=15, command=lambda: atualizar_estoque("add"))
# btn_add.pack(pady=5)

# btn_rem = tk.Button(janela, text="Remover Itens", bg="#F44336", fg="white", width=15, command=lambda: atualizar_estoque("rem"))
# btn_rem.pack(pady=5)

# janela.mainloop()

# 15.Relatório de Turno Completo:

# import tkinter as tk
# from tkinter import messagebox
# from tkinter import simpledialog

# # Configuração oculta para o Tkinter funcionar sem abrir uma janela vazia atrás
# root = tk.Tk()
# root.withdraw()

# TOTAL_PECAS = 5
# pecas_aprovadas = 0

# # Loop 'for' tradicional para processar as 5 peças
# for i in range(1, TOTAL_PECAS + 1):
#     # Abre uma caixinha pedindo o diâmetro da peça
#     diametro = simpledialog.askfloat(f"Peça {i}", f"Digite o diâmetro da peça {i} (em mm):")
    
#     # Se o usuário clicar em "Cancelar", o programa para
#     if diametro is None:
#         messagebox.showwarning("Cancelado", "Processo interrompido pelo usuário.")
#         exit()

#     # Validação do diâmetro (entre 19.9 e 20.1)
#     if 19.9 <= diametro <= 20.1:
#         pecas_aprovadas += 1

# # Cálculo da eficiência
# porcentagem_eficiencia = (pecas_aprovadas / TOTAL_PECAS) * 100

# # Exibe o relatório final em uma caixinha de mensagem
# mensagem_final = (
#     f"Total de peças aprovadas: {pecas_aprovadas} de {TOTAL_PECAS}\n"
#     f"Eficiência do lote: {porcentagem_eficiencia:.1f}%"
# )

# messagebox.showinfo("Relatório de Turno", mensagem_final)