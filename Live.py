def welcome(name=""):
    def printName(name):
        print(str.replace("<name>", name))

    str = "Hello <name> and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    if(name):
        printName(name)
    else:
        while(not name):
            name = input("Please enter your name:")
            if(name):
                printName(name)


def load_game():
    print("the game is starting")


welcome("Ran")
load_game()
