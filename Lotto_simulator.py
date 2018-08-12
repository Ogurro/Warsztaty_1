import random


def generate_winning_numbers():
    return random.sample(range(1, 50), 6)


def check_input(check_numb):
    try:
        check_numb = int(check_numb)
    except ValueError:
        return False
    else:
        return check_numb not in numb_list and 0 < check_numb < 50


def check_win(check_numbs, win_numbs):
    rv = 0
    for i in range(6):
        if check_numbs[i] in win_numb:
            rv += 1
    return rv


numb_list = []
i = 1
while i < 7:
    user_numb = input(f'Insert {i} number: ')
    if check_input(user_numb):
        numb_list.append(int(user_numb))
        i += 1
    else:
        print('Wrong input, try again')
numb_list = sorted(numb_list)
print("Your numbers: {}".format(' '.join(map(str, numb_list))))

win_numb = sorted(generate_winning_numbers())
print("Wining numbers {}".format(' '.join(map(str, win_numb))))

hits = check_win(numb_list, win_numb)
if hits > 2:
    print(f'Winner, You got {hits} numbers!')
else:
    print(f'sorry, You missed {6-hits} numbers')
