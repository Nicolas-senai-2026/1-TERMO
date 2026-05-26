# nome = input("Digite o nick que deseja no jogo!:  ")
# nivel = input("Digite o seu nivel atual no jogo!:   ")
# print(f"O jogador {nome} está no nível {nivel} e pronto para partida!")

# vs = float (input("Quanto você ganha por semana?:   "))
# total = vs * 4
# print(f"Sua mesada no fim do mês foi de... {total}")

# gb = float("Digite o valor em Gigabytes:  ")
# mb = gb * 1024
# print(f"O valor convertido em Megabytes seria de... {mb}")

# print("Média das notas")
# mat = float("Digite sua nota de Matemática:   ")
# port = float("Digite sua nota de Português:   ")
# media = (mat + port) /2
# print(f"Sua média das duas matérias foi de {media}")

# sa = int(input("Quantos seguidores você tem possui?:   "))
# sn = int(input("Quantos novos seguidores você ganhou?:   "))
# total = sa + sn
# print(f"Você possui {total} um total atualizado de seguidores!!")

# print("Seja Bem-Vindo aluno!! Vamos conferir sua idade!!!!")
# idade = int(input("Digite sua idade para nós calcular quantos dias você ja viveu:   "))
# total = (idade * 365)
# print("Aqui está o total de dias que você ja viveu aluno:", total)
# print("Espero que tenha gostado aluno, até a próxima!!!!!!!")

# print("Bem-Vindo ao Lanche do Senai!!!!!")
# pergunta1 = int(input("Qual o valor do salgado garçom?:    "))
# pergunta2 = int(input("Qual o valor do suco também por favor?:   "))
# conta = (pergunta1 + pergunta2)
# print("A sua conta deu:", conta)
# print("Espero que você tenha gostado do nosso lanche!!!!!! VOLTE SEMPRE!")

# print("Seja Bem-Vindo ao seu Ano de Nascimento!")
# ano = int(input("Digite qual o ano que você está agora:   "))
# idade = int(input("Digite sua idade atual:   "))
# soma = (ano - idade)
# print("Seu ano de nascimento é de:",  soma)
# print("Espero que você tenha gostado, volte sempre!!!!!")

# print("Seja Bem-Vindo ao filtro de idade do TikTok")
# idade = int(input("Digite sua idade para o TikTok avaliar você:   "))
# if idade < 13:
#     print("Você não pode acessar esse site (Acesso Restrito) ")
# elif 13 < idade < 18:
#     print("Você não pode aceesar tudo do site mais consegue ver algumas coisas (Acesso Moderado)")
# else:
#     print("Você pode entrar no site e fazer tudo (Acesso liberado)")
# print("Espero que tenha gostado, se você não conseguiu aceesar por idade, volte daqui alguns anos!!!!!!")

# print("Olá, hoje iremos monitorar a bateria do seu smartphone!!")
# import time 
# bateria = 100
# LIMITE_ALERTA = 20 
# INCREMENTO = 5 
# print("\n--- Monitoramento de Bateria Ativado ---")
# while bateria < LIMITE_ALERTA:
#     print(f"Bateria atual: {bateria}%. Sistema operando normalmente...") 
# time.sleep(1) # Espera meio segundo para simular o tempo real 
# bateria += INCREMENTO # Simulação de aquecimento 
# if bateria >= LIMITE_ALERTA - INCREMENTO: # Alerta de Pré-Limite 
#     print("AVISO: Atingindo bateria crítica em breve.") 
# print(f"ALERTA! Bateria atingiu o limite {bateria}%. Conecte-se ao carregador!")


# foto = ["1", "2", "3", "4", "5"]

# for curtidas in foto: 
#     print(f"Curtida n°: {curtidas} recebida.") # Simulação de processamento 
# if curtidas == "5": 
#     print("Contando quantas curtidas você obteve na fotoo...") 
# print(f"Você obteve curtidas {curtidas} contadas com sucesso!")
# print("Fim do processamento de curtidas na sua foto.")

# print("Carrinho de Compras Online")
# print("Digite sair para encerrar o Sistema ")
# contador = 0
# produto = ""

# while produto != "sair":
#     contador =+ 1
#     produto = input("Digite o nome do produto ou sair para finalizar...")
#     if produto.lower != "sair":
#         print(f"Produto {produto} adicionado ao carrinho!")

# print(f"Compra finalizada você adicionou {contador} itens ao seu carrinho!")
# print("Obrigado por comprar conosco!")

# print("Carrinho de compras online 2.0")
# contador = 0 
# produto = 0 
# while produto != "sair":
#     contador =+ 1
#     produto = input("Digite o nome do produto ou sair para finalizar")
# print(f"Você adicionou {contador-1} itens ao carrinho")
# print("Obrigado por comprar conosco!")