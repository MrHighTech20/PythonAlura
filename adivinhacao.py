print("********************************")
print("Bem vindo ao jogo de Adivinhacao")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

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
            print("Voce errou, su chute foi menor que o numero secreto")

print("Fim do jogo")
