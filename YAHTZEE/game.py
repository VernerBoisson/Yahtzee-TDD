def find_by_combination(dice_tuple, number_combination):
    sum = 0
    for i in dice_tuple:
        if i == number_combination:
            sum += number_combination
    return sum

def three_of_a_kind(dice_tuple):
    for i in dice_tuple:
        if dice_tuple.count(i) >= 3:
            return sum(dice_tuple)
    return 0

def four_of_a_kind(dice_tuple):
    for i in dice_tuple:
        if dice_tuple.count(i) >= 4:
            return sum(dice_tuple)
    return 0

def yahtzee():
    return 0

def full_house():
    return 0

def small_straight():
    return 0

def large_straight():
    return 0

def chance():
    return 0
