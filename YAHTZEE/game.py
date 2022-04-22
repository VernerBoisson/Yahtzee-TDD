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

def full_house():
    return 0

def small_straight():
    return 0

def large_straight():
    return 0