print("********************************")
print("Bem vindo ao jogo de Adivinhacao")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou:", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou")
    else:
        if(maior):
            print("Voce errou, seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou, su chute foi menor que o numero secreto")

print("Fim do jogo")
