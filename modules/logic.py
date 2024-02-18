import random
from decouple import config

started_capital_of_gambler = config('MY_MONEY', default=1000, cast=int)
gamblers_capital = started_capital_of_gambler
slots = list(range(1, 11))


def get_user_input():
    while True:
        try:
            choose_slot = int(input('Select your bet slot (1-10): '))
            bid = int(input('Enter your bid: '))
            print('_______________________________________')
            if choose_slot not in slots or bid > gamblers_capital or bid < 0:
                print('Invalid input. Try again.')
                continue

            return choose_slot, bid

        except ValueError:
            print('Invalid input. Try again.')


def spin_wheel():
    print('Spinning the wheel...')
    return random.choice(slots)


def evaluate_result(choose_slot, result):
    if choose_slot == result:
        print(f'Congratulations! You won and your bid is doubled.')
        return 2
    else:
        print('Sorry, you lost your bet.')
        return -1


def play_game():
    global gamblers_capital

    while True:
        print(f'Your current balance: {gamblers_capital}$')
        choose_slot, bid = get_user_input()

        result = spin_wheel()
        print(f'The winning slot is: {result}')

        multiplier = evaluate_result(choose_slot, result)
        gamblers_capital += bid * multiplier

        print(f'Your account at the moment: {gamblers_capital}$\n'
              f'_______________________________________')

        play_again = input('Do you want to play again? (y/n): ')
        print('_______________________________________')
        if play_again.lower() != 'y':
            break


def print_final_result():
    print(f'You started with: {started_capital_of_gambler}$ and ended with: {gamblers_capital}$')
    print('Game over. Thanks for playing!')
