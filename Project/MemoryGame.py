import random
import time
from Colors import bcolors
from Utils import Screen_cleaner


def generate_sequence(level):
    rand_list = []
    for i in range(level):
        rand_list.append(random.randint(i+1, level))

    print(f"The number is:\n{rand_list}")
    time.sleep(0.7)
    Screen_cleaner()
    return rand_list


def get_list_from_user(level):
    rand_list = []
    validation = False
    while validation == False:
        try:
            number = int(input("Please enter a number:\n"))
            rand_list.append(number)
            if (rand_list.__len__() == level):
                validation = True
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)

    return rand_list


def is_list_equal(game_list, user_list):
    return set(game_list) == set(user_list)


def play(difficulty):
    list_numbers = generate_sequence(difficulty)
    list_users = get_list_from_user(difficulty)
    return is_list_equal(list_numbers, list_users)


def load_memory_game(difficulty):
    return play(difficulty)
