import re
from utils import get_input_lines

def clean_memory(corrupt_instructions):
    pattern = r"mul\((\d+),(\d+)\)"
    pairs = []
    for row in corrupt_instructions:
        pairs += re.findall(pattern, row)
    return pairs

def multiply_pairs(instructions):
    products = [int(x) * int(y) for x, y in instructions]
    return products

if __name__ == "__main__":
    test = False
    test_data = get_input_lines(3, test)
    good_instructions = clean_memory(test_data)
    executed_instructions = multiply_pairs(good_instructions)
    all_instructions = sum(executed_instructions)
    print(all_instructions)