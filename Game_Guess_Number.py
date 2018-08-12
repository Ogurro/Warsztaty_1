import random


def generate_number(start=1, end=100):
    return random.randint(start, end)


def get_number():
    return input('Guess number: ')


valid_number = generate_number()
while True:
    guess_number = get_number()
    try:
        guess_number = int(guess_number)
    except ValueError:
        print('It\'s not a number')
    else:
        if guess_number < valid_number:
            print('Too small number!')
        elif guess_number > valid_number:
            print('Too big number!')
        else:
            print('Nice, You guessed number')
            break
