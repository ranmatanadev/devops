from Colors import bcolors
from CurrencyRouletteGame import load_roulette_game
from GuessGame import load_guess_game
from MemoryGame import load_memory_game
from Score import add_score


def welcome(name=""):
    sentence = "\nHello <name> and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    if (name):
        return sentence.replace("<name>", name)+"\n"
    else:
        while (not name):
            name = input("\nPlease enter your name:")
            if (name):
                return sentence.replace("<name>", name)+"\n"


def check_result(level, status):
    if (status == True):
        add_score(level)
    else:
        print("You Lose!")


def load_game():
    validation = False
    while validation == False:
        try:
            choose_game = int(input("\nPlease choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
            if 1 <= choose_game <= 3:
                validation = True
            else:
                print(bcolors.FAIL +
                      "\nPlease enter a number between 1-3\n" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)
    validation = False
    while validation == False:
        try:
            choose_difficulty = int(
                input("\nPlease choose game difficulty from 1 to 5:\n"))
            if 1 <= choose_difficulty <= 5:
                validation = True
            else:
                print(bcolors.FAIL +
                      "\nPlease enter a number between 1-5\n" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)

    match choose_game:
        case 1:
            check_result(choose_difficulty,
                         load_memory_game(choose_difficulty))
        case 2:
            check_result(choose_difficulty, load_guess_game(choose_difficulty))
        case 3:
            check_result(choose_difficulty,
                         load_roulette_game(choose_difficulty))
        case _:
            return 0
