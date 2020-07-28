# jogo que desafia o jogador a descobrir o número secreto.

import random
from sys import exit

def init_lang():
    print("Choose language / Escolha o idioma")
    print("1 - English")
    print("2 - Português")
    while True:
        lang = input('> ')
        if "1" in lang:
            guess_en()
        elif "2" in lang:
            guess_pt()
        else:
            print("Type 1 for English / Digite 2 para Português")

def play_again_pt():
    print("Quer jogar novamente?")
    while True:
        play = input('> ')
        if "sim" in play.lower():
            guess_pt()
        elif "não" in play.lower():
            print("Até breve!")
            exit(0)
        else:
            print("Sim ou Não?")

def play_again_en():
    print("Wanna play again?")
    while True:
        play = input('> ')
        if "yes" in play.lower():
            guess_en()
        elif "no" in play.lower():
            print("See you soon!")
            exit(0)
        else:
            print("Yes or No?")

def guess_pt():
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
                    play_again_pt()
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
                    print("Como você chegou aqui? Digite um número de 1 a 20.")
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
            play_again_pt()

def guess_en():
    numero_secreto = random.randrange(1, 21)
#   print(numero_secreto)
    chances = 3
    print("What's your name?")
    nome = input('> ')
    print(f"Welcome, {nome}! This is a simple guess game. I've just thought of a number between 1 and 20.")
    print("Let's see if you can guess the number?")
    print("You've got 3 chances.")
    while True:
        if chances > 0:
            chute = input('> ')
            if chute.isnumeric():
                chute = int(chute)
                if chute == numero_secreto:
                    print(f"Awesome, {nome}! You got it right! Congratulations!")
                    print("")
                    print("This game was developed by Marcus Couto.")
                    print("twitter.com/marcvs")
                    print("mvcoutob@gmail.com")
                    print("github.com/m-cout")
                    play_again_en()
                elif (chute < 1) or (chute > 20):
                    print("I said number between 1 and 20 only!")
                elif chute < numero_secreto:
                    chances -= 1
                    print("Wrong. The number is greater than that.")
                    print(f"Remaining chances: {chances}!" )

                elif chute > numero_secreto:
                    chances -= 1
                    print("Wrong. The number is smaller than that.")
                    print(f"Remaining chances: {chances}!" )

                else:
                    print("How did you get here? Type a number between 1 and 20.")
            else:
                print("You must type a number!")
        else:
            print(f"Sorry, {nome}, but you ran out of chances.")
            print(f"The secret number was {numero_secreto}! Maybe next time?")
            print("")
            print("This game was developed by Marcus Couto.")
            print("twitter.com/marcvs")
            print("mvcoutob@gmail.com")
            print("github.com/m-cout")
            play_again_en()

init_lang()
