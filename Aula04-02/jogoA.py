import random

def jogo():
    print("Bem-Vindo ao jogo de adivinhação!!!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5

    while tentativas < max_tentativas:
        palpite = int(input("Digite um número: "))
        tentativas = tentativas + 1
        
        if palpite == numero_secreto:
            print("Ganhou!")
            break
        elif palpite > numero_secreto:
            print("Tente um número menor")
        elif palpite < numero_secreto:
            print("Tente um número maior")

    if tentativas == max_tentativas:
        print(f"PERDEU, número secreto era {numero_secreto}")

jogo()