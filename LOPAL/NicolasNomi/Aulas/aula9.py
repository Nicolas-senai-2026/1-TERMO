# fazer = ["Chegar","Abaixar","Retirar a peça","Voltar"]
# print("Olá funcionario, tenho um trabalho para você concluir.")
# missao = input("Você ira andar até a moto cinza e pegar a peça vermelha e trazer para mim.")
# passos = input("Você dará 50 passos.")
# if passos in missao: 
#     print(f"Você dará 25 passos para chegar moto e irá {fazer} peça vermelha")
#     elif:
#     print("Você dará 25 passos para voltar e entregar a peça para mim.")
#     else:
#         print("Error...")
# print("Seu trabalho foi concluido com sucesso, irei lhe convocar mais vezes.")

# corrigido

# fazer = ["Chegar", "Abaixar", "Retirar a peça", "Voltar"]

# print("Olá funcionario, tenho um trabalho para você concluir.")

# missao = input("Você irá andar até a moto cinza e pegar a peça vermelha e trazer para mim.\n")
# passos = int(input("Você dará quantos passos?:  "))

# if passos == 25:
#     print("Você dará 25 passos para chegar na moto e irá retirar a peça vermelha.")
# elif passos > 25:
#     print("Você deu passos demais, revise o caminho.")
# else:
#     print("Você deu poucos passos, não chegou até a moto.")

# print("Seu trabalho foi concluído com sucesso, irei lhe convocar mais vezes.")

# Projeto: Gerenciamento de Cancela de Shopping

# --- Entrada do Estacionamento ---
placa = input("Placa: ")
tag = input("Possui TAG? (s/n): ").lower()

if tag == 's':
    print(f"Acesso liberado (TAG) para {placa}.")
else:
    print(f"Ticket emitido para {placa}.")

# --- Saída do Estacionamento ---
print("\n--- Saída ---")
tempo = float(input("Horas de permanência: "))
valor_hora = 10.00 
total = tempo * valor_hora

print(f"Total a pagar: R$ {total:.2f}")

if tag == 's':
    print("Cobrado na fatura automática. Saída liberada.")
else:
    input("Pagar no totem (enter após pagar)...")
    print("Saída liberada.")

