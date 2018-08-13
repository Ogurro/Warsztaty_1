def calculate_guess(minimum, maximum):
    return int((maximum - minimum) / 2) + minimum


def user_input(msg):
    while True:
        answer = input(msg)
        if answer.lower() == 'y' or answer.lower() == 'n':
            break
        print('Wrong input')
    return answer


print("Think of number between 0 and 1000 and i\'ll guess it in 10 moves")
guess_min = 0
guess_max = 1000

while True:
    guess = calculate_guess(guess_min, guess_max)
    if guess == 0:
        print('You are cheater! :(')
        break
    if guess_min == 999:
        guess = 1000
        print(f'my finnal guess is {guess} or you are cheating')
        break
    if guess_min == guess_max:
        print('you are cheating!')
        break
    print(f"Guessing: {guess}")
    user_guess = user_input("Am I correct? [y/n]: ")
    if user_guess.lower() == 'y':
        print("I won!")
        break
    else:
        user_guess = user_input("Too muich? [y/n]: ")
        if user_guess.lower() == 'y':
            guess_max = guess
        else:
            user_guess = user_input("Too little? [y/n]: ")
            if user_guess.lower() == 'y':
                guess_min = guess
            else:
                print("Don't cheat!")
