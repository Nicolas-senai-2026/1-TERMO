# 1. O Laço ´for` (Repetições Determinadas)
# Use o ´for` quando você sabe exatamente qunatas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um: 

# # Exemplo 1 
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada")
    
# # Exemplo 2
# for b in range(10): 
#     print(f"Quantidade total {b}  foi...")


# Exemplo 3 
# Imagine o seguinte cenário, iremos produzir 20 discos de vuinil.

# for discos in range(1, 21):
#     print(f"Processando a produção de discos de vinil {discos}  foi...")
#     print("Quantidade verificada com sucesso ")
#     print("A produção foi um sucesso")


# # Exemplo 4 
# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# itempeças = ["Cilindrico", "Eixo Cônico", "Radiais", "Madeira", "Bola", "Cabeça Chata", "Chave Metalica Verde"]
# for itens in peças:
#     print(f"Item em estoque: {itens}")
# for itens2 in itempeças:
#     print(f"Item de peças em estoque: {itempeças}")


# Exemplo 5 Imagine a seguinte situação, gostaria de ter um menu onde pudesse perguntar qual opção deseja e a partir da seleção ele listar os produtos

# print("Barber-House")
# print("Opção 1- Peças")
# print("Opção 2- Item Peças")
# menu = int(input("EScolha uma das opções   "))

# peças = ["Maquina", "Tesoura", "Navalha", "Cadeira", "Espanador", "Pente"]
# itempeças = ["Degrade","Tirar Volume", "Mais raspado", "Onde o cliente senta", "Limpar o clinte", "Facilitar o corte"]

# if menu == 1: 
#     for item1 in peças:
#         print(f"Sua lista de peças {peças} são...")
# elif menu == 2: 
#     for item2 in peças:
#         print(f" Sua lista de itens de peças {itempeças} são...")
# else:
#      print("Opção inválida: Encerrando o sistema")



# # Exercicio 1
# # 1. Contador de Proodução (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para casda numero, imprima "Peça numero X processada com sucesso". No final, exiba "Ciclo de produção concluido"




# for ciclo in range(1,11):
#     print(f"Peça nº {ciclo} processada com sucesso...")
#     print("Ciclo de prodeção concluida...")


# Exercicio 2 
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, abacaxi.

# Exercicico 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta


# frutas = ["Banana", "Manga", "Melancia", "Abacaxi"]
# quantidade = ["10", "5", "10", "13"]
# for banana in range(1, 10):
#     print(f"A quantidade da {banana}  foi realizada... ")
# for manga in range(1, 6):
#     print(f"A quantidade da {manga}  foi realizada... ")
# for melancia in range(1, 10):
#     print(f"A quantidade da {melancia}  foi realizada... ")
# for abacaxi in range(1, 14):
#     print(f"A quantidade da {abacaxi}  foi realizada... ")
#  soma1 = int(input("Digite o primeiro valor:    "))
#  soma2 = int(input("Digite o segundo valor:    "))
#  soma3 = int(input("Digite o terceiro valor:    "))
#  soma4 = int(input("Digite o quarto valor:    "))
# total = soma1 + soma2 + soma3 + soma4
# print("A soma é:", total)


# print("Bem-Vindo a Tabuada Visual Code")
# print("EScolha qual a tabuada que você deseja")
# (print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))
# tabuada0 = input("Digite o numero da tabuada que deseja:   ")
# tabuada1 = int(input("Digite o primeiro valor:    "))
# tabuada2 = int(input("Digite o segundo valor:     "))
# total = tabuada1 * tabuada2
# print("O resultado da tabuada escolhida é:", total)


# print("Bem-Vindo a Tabuada Visual Code")
# print("EScolha qual a tabuada que você deseja")
# (print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))
# for tabuada in range(1, 11):
#     print(f"Tabuada do (1)")
#     tabuada1 = ["1x1", "1x2", "1x3", "1x4", "1x5", "1x6", "1x7", "1x8", "1x9", "1x10"]
#     resultado1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
# for tabuada in range(1, 11):
#     print(f"Tabuada do (2)")
#     tabuada2 = ["2x1", "2x2", "2x3", "2x4","2x5", "2x6", "2x7", "2x8", "2x9", "2x10"]
#     resultado2 = ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20"]


    
