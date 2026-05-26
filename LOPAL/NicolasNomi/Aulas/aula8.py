# Exercícios de Programação Python: "O Caça-Erros"

# 1.0 O problema da idade
#erro
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade")

#corrigido
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print(f"Você tem a idade certa. Liberado!")

#melhorado
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print(f"Você tem a idade certa. Liberado!")
# else:
#     print("Você é menor de idade. Recusado!")

# 2. A Escrita Fiel
# errado
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# melhorado
# print("Olá")
# nome = input("Digite seu Nome: ") 
# print(f"Seja Bem-Vinda ao Site, {nome}")

#errado
# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# #corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

#melhorado
# numero = int(input("Digite um número: ")) 

# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

#errado
# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

#corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

#melhorado
# tentativa = int(input("Bem-Vindo!"))
# usuario_cadastrado = int(input("Digite seu usuario:  "))
# if tentativa == usuario_cadastrado:
#     print("Login realizado com sucesso. Bem-vindo!")
# else:
#     print("Usuário incorreto. Acesso negado.")

#errado
# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#corrigido
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

#melhorado
# clima = input("Como está o clima hoje? (ensolarado/chuvoso): ")

# if clima == "chuvoso":
#     print(" Leve um guarda-chuva!")
# elif clima == "ensolarado":
#     print(" Aproveite o sol e use protetor solar!")
# else:
#     print(" Clima interessante! Aproveite o seu dia.")

#errado
# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

#corrigido
# pontos = 50
# print(f"Parabens! Você fez {pontos} + {pontos}. ")

#melhorado
# pontos = int(input("Digite quantos pontos você fez:  "))
# print(f"Parabens! Você fez {pontos} + {pontos}. ")

#errado
# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

#corrigido
# nota = 9.5
# if nota >= 7:
#     print("Aprovado!")
# elif nota >= 9:
#     print("Excelente!!")

#melhorado
# entrada = input("Digite a nota do aluno (0 a 10): ")
# nota = float(entrada)

# if nota >= 9:
#     print("Excelente!!")
# elif nota >= 7:
#     print("Aprovado!")
# else:
#     print("Reprovado. Precisa estudar mais!")

#errado
# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

#corrigido
# for i in range(5):
#     print(f"{i}")

#melhorado
# print("Seja Bem-Vindo ao contador de 1-5")
# for i in range(5):
#     print(f"{i}")
# print("Tomara que tenha gostado do contador! Volte sempre.")

#errado
# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

#corrigido
# while tentativas <= 3:
#     print(f"Tentativa {tentativas}: Tentando conectar...")
#     tentativas += 1 

# print("Falha na conexão após 3 tentativas.")

#melhorado
# print("Seja Bem-Vindo ao Loop Eterno")
# for tentativa in range(1, 4):
#     print(f"Tentando conectar... (Carga: {tentativa}/3)")
# print("Processo finalizado.")
# print("Volte novamente!!")
#errado
# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

#corrigido
# senha = ""
# while senha == "phyton123":
#     senha = int(input("Digite a senha secreta:  "))
# print("Acesso Liberado.")

#melhorado
# print("Seja Bem-Vindo ao Site secreto de senhas.")
# # senha = ""
# # while senha == "phyton123":
# #     senha = int(input("Digite a senha secreta:  "))
# # print("Acesso Liberado.")
# print("Se você gostou volte novamente!!")