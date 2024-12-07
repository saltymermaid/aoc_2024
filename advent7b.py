from utils import get_input_lines
from advent7a import parse_input, add, multiply

def concat(x, y):
    str_x = str(x)
    str_y = str(y)
    return int(str_x + str_y)

def can_reach_target(operators):
    target, numbers = operators
    first_num = numbers[0]
    second_num = numbers[1]
    if len(numbers) == 1:
        return first_num == target
    added = add(first_num, second_num)
    multiplied = multiply(first_num, second_num)
    concatenated = concat(first_num, second_num)
    if len(numbers) == 2:
        if added == target:
            return True
        if multiplied == target:
            return True
        if concatenated == target:
            return True
        return False
    else:
        new_add = [added]
        new_add.extend(numbers[2:])
        if can_reach_target([target, new_add]):
            return True
        new_mult = [multiplied]
        new_mult.extend(numbers[2:])
        if can_reach_target([target, new_mult]):
            return True
        new_concat = [concatenated]
        new_concat.extend(numbers[2:])
        if can_reach_target([target, new_concat]):
            return True
    return False


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('7', test)
    operations = parse_input(input_data)
    fixable_operations_total = 0
    for operation in operations:
        if can_reach_target(operation):
            fixable_operations_total += operation[0]
    print(fixable_operations_total)
