class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def welcome(name=""):
    sentence = "\nHello <name> and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    if(name):
        return sentence.replace("<name>", name)+"\n"
    else:
        while(not name):
            name = input("\nPlease enter your name:")
            if(name):
                return sentence.replace("<name>", name)+"\n"


def load_game():
    validation = False
    while validation == False:
        try:
            choose = int(input("\nPlease choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
            if 1 <= choose <= 3:
                validation = True
            else:
                print(bcolors.FAIL +
                      "\nPlease enter a number between 1-3\n" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)
    validation = False
    while validation == False:
        try:
            choose = int(
                input("\nPlease choose game difficulty from 1 to 5:\n"))
            if 1 <= choose <= 5:
                validation = True
            else:
                print(bcolors.FAIL +
                      "\nPlease enter a number between 1-5\n" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)
