from utils import get_input_lines

def parse_input(input_data):
    operations = []
    for row in input_data:
        test_value, raw_operands = row.split(":")
        operands = [int(op) for op in raw_operands.split()]
        operations.append([int(test_value), operands])
    return operations

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def can_reach_target(numbers, target):
    if len(numbers) == 1:
        return numbers[0] == target
    added = add(numbers[0], numbers[1])
    multiplied = multiply(numbers[0], numbers[1])
    if len(numbers) == 2:
        if added == target:
            return True
        if multiplied == target:
            return True
        return False
    else:
        new_add = [added]
        new_add.extend(numbers[2:])
        if can_reach_target(new_add, target):
            return True
        new_mult = [multiplied]
        new_mult.extend(numbers[2:])
        if can_reach_target(new_mult, target):
            return True
    return False

def fix_op(operation):
    desired_value = operation[0]
    return can_reach_target(operation[1], desired_value)

if __name__ == "__main__":
    test = False
    input_data = get_input_lines('7', test)
    operations = parse_input(input_data)
    fixable_operations_total = 0
    for operation in operations:
        fixed = fix_op(operation)
        if fixed:
            fixable_operations_total += operation[0]
    print(fixable_operations_total)
