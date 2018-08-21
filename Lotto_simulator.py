import random


def generate_winning_numbers():
    return random.sample(range(1, 50), 6)


def check_input(check_numb, numb_list):
    try:
        check_numb = int(check_numb)
    except ValueError:
        return False
    else:
        return check_numb not in numb_list and 0 < check_numb < 50


def check_win(check_numbs, win_numbs):
    rv = 0
    for i in range(6):
        if check_numbs[i] in win_numbs:
            rv += 1
    if rv > 2:
        print(f'Winner, You got {rv} numbers!')
    else:
        print(f'sorry, You got {rv} numbers')


def get_user_numbers():
    numb_list = []
    i = 1
    while i < 7:
        user_numb = input(f'Insert {i} number: ')
        if check_input(user_numb, numb_list):
            numb_list.append(int(user_numb))
            i += 1
        else:
            print('Wrong input, try again')
    return numb_list


def print_numbers(list_of_numbs):
    print(' '.join(map(str, list_of_numbs)))


def sort(func):
    return lambda: sorted(func())


sorted_get_user_numbers = sort(get_user_numbers)
sorted_generate_winning_numbers = sort(generate_winning_numbers)

if __name__ == '__main__':
    user_numbs = sorted_get_user_numbers()
    winning_numbs = sorted_generate_winning_numbers()

    print_numbers(user_numbs)
    print_numbers(winning_numbs)

    check_win(user_numbs, winning_numbs)
