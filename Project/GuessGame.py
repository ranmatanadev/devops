import random
from Colors import bcolors


def generate_number(level):
    return random.randint(1, level)


def compare_results(user_guess, secret_number):
    try:
        if (user_guess == secret_number):
            return True
        else:
            return False
    except:
        return False


def get_guess_from_user(level):
    validation = False
    while validation == False:
        try:
            get_number = int(
                input(f"Please enter a number between 1-{level}:\n"))
            if 1 <= get_number <= level:
                validation = True
            else:
                print(bcolors.FAIL +
                      f"\nPlease enter a number between 1-{level}\n" + bcolors.ENDC)
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)

    return get_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    result = compare_results(user_number, secret_number)
    print("difficulty", difficulty)
    print("secret_number", secret_number)
    print("user_number", user_number)
    if (result):
        return True
    else:
        return False


def load_guess_game(difficulty):
    return play(difficulty)
