# jogo que desafia o jogador a descobrir o número secreto.

import random
from sys import exit

def jogo():
    numero_secreto = random.randrange(1, 21)
#   print(numero_secreto)
    chances = 3
    print("Qual o seu nome?")
    nome = input('> ')
    print(f"Olá, {nome}! Este é um jogo simples de adivinhação. Acabo de pensar em um número entre 1 e 20.")
    print("Vamos ver se você consegue adivinhar que número é esse?")
    print("Você tem 3 chances.")
    while True:
        if chances > 0:
            chute = input('> ')
            if chute.isnumeric():
                chute = int(chute)
                if chute == numero_secreto:
                    print(f"Genial, {nome}! Você acertou! Parabéns!")
                    print("")
                    print("Este jogo foi desenvolvido por Marcus Couto.")
                    print("twitter.com/marcvs")
                    print("mvcoutob@gmail.com")
                    print("github.com/m-cout")
                    exit(0)
                elif (chute < 1) or (chute > 20):
                    print("Eu disse número entre 1 e 20, apenas!")
                elif chute < numero_secreto:
                    chances -= 1
                    print("Você errou. Eu pensei em um número maior do que este.")
                    print(f"Tentativas restantes: {chances}!" )

                elif chute > numero_secreto:
                    chances -= 1
                    print("Você errou. Eu pensei em um número menor do que este.")
                    print(f"Tentativas restantes: {chances}!" )

                else:
                    print("O que foi isso? Eu disse números entre 1 e 20!")
            else:
                print("Você tem que digitar um número!")
        else:
            print(f"Lamento, {nome}, mas suas chances acabaram.")
            print(f"O número secreto era {numero_secreto}!")
            print("")
            print("Este jogo foi desenvolvido por Marcus Couto.")
            print("twitter.com/marcvs")
            print("mvcoutob@gmail.com")
            print("github.com/m-cout")
            exit(0)

jogo()
