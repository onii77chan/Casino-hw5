import random
from decouple import config

started_capital_of_gambler = config('STARTED_CAPITAL_OF_GAMBLER', default=1000, cast=int)
gamblers_capital = 1000
slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def start_game():
    global gamblers_capital, choose_slot, bid
    user_started_game = input('welcome to the casino want to start playing y/n?: ')
    if user_started_game == 'y':
        print(f'your account is currently {gamblers_capital}')
        try:
            choose_slot = int(input('ok now select your bet slot: '))
            bid = int(input('enter your bid: '))
        except ValueError:
            print('invalid input please try again: ')
        print('_____________________________')

        random_card()
        checking_conditions_for_winning()

    elif user_started_game == 'n':
        print('exit()')
        breakpoint()
    else:
        print('invalid input')


def checking_conditions_for_winning():
    global gamblers_capital
    if choose_slot == random_card():
        print(f'your bet was successful and it increased by 1.5')
        gamblers_capital += bid * 1.5
    elif choose_slot != random_card():
        print('your bet is not successful you lose your bet')
        gamblers_capital -= bid


def random_card():
    r_card = random.choice(slots)
    return r_card
