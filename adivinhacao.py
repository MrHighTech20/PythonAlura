import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhacao")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    print("Qual o nivel de dificuldade ?")
    print("(1) Facil (2) Medio (3) Difici")

    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou")
            break
        else:
            if(maior):
                print("Voce errou, seu chute foi maior que o numero secreto")
            elif(menor):
                print("Voce errou, seu chute foi menor que o numero secreto")

    print("Fim do jogo")
    
if(__name__ == "__main__"):
    jogar()