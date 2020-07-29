# a game that challenges the player to guess a secret number.

import random
from sys import exit

# asks in which language the player wants to play
def init_lang():
    print("Choose language / Escolha o idioma")
    print("1 - English")
    print("2 - Português")
    while True:
        lang = input('> ')
        if "1" in lang:
            name_en()
        elif "2" in lang:
            name_pt()
        else:
            print("Type 1 for English / Digite 2 para Português")

# gets user name (english)
def name_en():
    print("What's your name?")
    nome = input('> ')
    guess_en(nome)

# gets user name (portuguese)
def name_pt():
    print("Qual o seu nome?")
    nome = input('> ')
    guess_pt(nome)

# asks if the player wants to play again, restart the game if positive, exit if negative (english)
def play_again_en(nome):
    print("Wanna play again?")
    while True:
        play = input('> ')
        if "yes" in play.lower():
            guess_en(nome)
        elif "no" in play.lower():
            print("Thanks for playing! See you soon!")
            exit(0)
        else:
            print("Yes or No?")

# asks if the player wants to play again, restart the game if positive, exit if negative (portuguese)
def play_again_pt(nome):
    print("Quer jogar novamente?")
    while True:
        play = input('> ')
        if "sim" in play.lower():
            guess_pt(nome)
        elif "não" in play.lower():
            print("Obrigado por jogar! Até breve!")
            exit(0)
        else:
            print("Sim ou Não?")

# this is the main structure of the game (english)
def guess_en(nome):
    numero_secreto = random.randrange(1, 21)
#   print(numero_secreto)
    chances = 3
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
                    print("")
                    play_again_en(nome)
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
            print("")
            play_again_en(nome)

# this is the main structure of the game (portuguese)
def guess_pt(nome):
    numero_secreto = random.randrange(1, 21)
#   print(numero_secreto)
    chances = 3
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
                    print("")
                    play_again_pt(nome)
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
            print("")
            play_again_pt(nome)

init_lang()
