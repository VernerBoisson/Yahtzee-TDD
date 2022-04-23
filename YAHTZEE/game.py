def find_by_combination(dice_tuple, number_combination):
    sum = 0
    for i in dice_tuple:
        if i == number_combination:
            sum += number_combination
    return sum

def find_number_of_a_kind(dice_tuple, number_of_a_kind):
    for i in dice_tuple:
        if dice_tuple.count(i) >= number_of_a_kind:
            if number_of_a_kind == 5:
                return 50
            return sum(dice_tuple)
    return 0

def full_house(dice_tuple):
    if dice_tuple.count(dice_tuple[0]) == 2 and dice_tuple.count(dice_tuple[1]) == 3:
        return 25
    return 0

def find_straight(dice_tuple, straight_type):
    if straight_type == 'small':
        if all(i in dice_tuple for i in [1, 2, 3, 4]) or \
            all(i in dice_tuple for i in [2, 3, 4, 5]) or \
            all(i in dice_tuple for i in [3, 4, 5, 6]):
            return 30
    elif straight_type == 'large':
        if all(i in dice_tuple for i in [1, 2, 3, 4, 5]) or \
            all(i in dice_tuple for i in [2, 3, 4, 5, 6]):
            return 40
    return 0