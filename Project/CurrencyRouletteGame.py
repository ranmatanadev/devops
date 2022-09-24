import requests
from Colors import bcolors
import json


def get_money_interval(amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=ILS&amount={amount}"
    payload = {}
    headers = {
        "apikey": "XctY2ZtBpZlByIJb7xZrQItPPhcpClRA"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    if (status_code == 200):
        result = response.text
        return json.loads(result)["result"]
    else:
        return False


def get_guess_from_user():
    validation = False
    while validation == False:
        try:
            number = float(input("\nPlease enter a number:\n"))
            return number
        except:
            print(bcolors.FAIL + "\nPlease enter a number\n" + bcolors.ENDC)


def play(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()

    if interval == guess:
        return True
    else:
        return False


def load_roulette_game(difficulty):
    return play(difficulty)
