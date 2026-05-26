# clean code - Aula 6
# Para que usar?
# Como usar?
# print("Clan Code - Aula 6")
# aula = 6
# print(f"Estamos na Aula {aula} de clean code")

# Manipulação de arquivos e texto
# texto = "  Phyton é muito legal!  "
# print(texto.strip().upper()) #"PHYTON"
# print(texto.strip().lower()) #"Phyton"
# print(texto.strip().capitalize()) #"Phyton"
# print(texto.strip().title()) #"Phyton"
# print(texto.strip().replace(" ","_")) #"Phyton"
# print(texto.strip().split()) # ["Phyton"]

# Escrevendo
# 

# Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# EXERCICIO 1 
# crie um programa que peça ao usuario para inserir uma frase e, em seguuida, exiba  a frase com as seguintes transfprmações:
# - Remova os espaços extras no ínicio e no final da frase

# print("Digite uma frase que deseja!")
# frase = input("Digite uma frase: ")

# frase_limpa = frase.strip()

# print("Frase processada:", frase_limpa)

# EXERCICIO 2
# crie um programa que leia o conteudo de um arquivo de txt e conte quantas vezes Palavra phyton aparece no arquivo Exiba o reultado para usuario.

# print("Contagem de palavras em arquivos")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Phyton")
#     print(f"A contagem de palavras {contagem} é de...")

# execução de comandos
# import os # importa o módulos os para interagir com o sistema operacional
# Onde estou?
# print(os.getcwd())
# listar arquivos na pasta
# print(os.listdir())
# print(os.listdir("..")) # lista arquivos da pasta pai
# print(os.listdir("..\\..")) # lista arquivos da pasta avo
# print(os.listdir("C:\\")) # lista arquivos da raiz do C
# print(os.listdir("C:\\Users")) # lista arquivos da pasta users
# print(os.listdir("C:\\Users\\Public")) # lista arquivos da pasta Public

# outros comandos uteis
# criar pasta
# os.mkdir("nova_pasta")
# # renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # excluir pasta
# os.rdmir("pasta_renomeada")

#Exercicio 2: 
# crie um script que mostre o caminho da pasta atual

#exercicio 3:
#liste um arquivo da pasta atual

#exercicio 4:
# crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta

# 2
# import os

# script = os.getcwd()
# print("Pasta atual:", script)

# # 3

# print(os.listdir(".."))

# # 4
# os.mkdir("projetos")
# os.rename("projetos","meus_projetos")
# os.rmdir("meus_projetos")

# exercicio 5
# crie um arquivo chamado "log.txt" e escrevva a mensagem "Log de Atividades"
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")
# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# exemplo de diciomario
# crie um dicionario com informações sobre uma pessoa e acessa um valor usando uma chave
# pessoa ={
#     "nome": "Bruno", 
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Engenharia",
# }
# pessoa ={
#     "nome": "Bruno", 
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "designer",
# }

# restaurante ={
#     "mesa": "5", 
#     "bebida": 2,
#     "comida": "2",
#     "comanda": "R$57,00",
# }
# padaria ={
#     "pao": "5", 
#     "cafe": 2,
#     "bolo": "1",
#     "conta": "R$57,00",
# }

# exemplo 2
# with open("desliga.bat", "w") as desligar:
#     desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho"\"")
#                    # -s comando para desligar
#                    # -t tempo para definir"
#                    # -a cancelar desligamento
# # with open("desliga.bat", "r") as desligar:
