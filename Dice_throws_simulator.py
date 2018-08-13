import re
import random


def throw_validation(text_valid):
    expr = r'(\d*)([D]\d+)+([-+]\d+)?'
    throw_valid = re.findall(expr, text_valid, re.I)
    if throw_valid:
        throw_valid = list(throw_valid[0])
    return throw_valid


def throw_numbers(throw_text):
    return int(throw_text if throw_text else 1)


def dice_type(dice_text):
    number_of_sides = int(dice_text.lower().replace('d', ''))
    valid_dices = (3, 4, 6, 8, 10, 12, 20, 100)
    if number_of_sides not in valid_dices:
        return None
    return number_of_sides


def throw_medicate(throw_addition):
    return int(throw_addition.replace('+', '')) if throw_addition else 0


def throw_action(throws, dice, bonus):
    throw_sum = sum(random.randint(1, dice) for _ in range(throws))
    throw_sum += bonus
    return throw_sum


def throw_simulation(text):
    throw_valid = throw_validation(text)
    if not throw_valid:
        return 'wrong input'
    type_of_dice = dice_type(throw_valid[1])
    if not type_of_dice:
        return 'Not valid type of dice'
    number_of_throws = throw_numbers(throw_valid[0])
    throw_bonus = throw_medicate(throw_valid[2])
    return throw_action(number_of_throws, type_of_dice, throw_bonus)


if __name__ == '__main__':
    throw = '2D10+10'
    print(throw, throw_simulation(throw))
    throw = 'D6'
    print(throw, throw_simulation(throw))
    throw = '2d3'
    print(throw, throw_simulation(throw))
    throw = 'd12-1'
    print(throw, throw_simulation(throw))
    throw = '2D11+10'
    print(throw, throw_simulation(throw))
