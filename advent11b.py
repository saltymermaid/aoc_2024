from collections import defaultdict
import copy
import math
from utils import get_input_string

def make_stones(input_data):
    return [int(stone) for stone in input_data.split(" ")]

def blink(stone):
    new_stones = []
    if stone == 0:
        new_stones.append(1)
    else:
        num_digits = math.floor(math.log10(stone)+1)
        if num_digits % 2 == 0:
            half = num_digits // 2
            first_half = stone // (10 ** half)
            second_half = stone % (10 ** half)
            new_stones.extend([first_half, second_half])
        else:
            new_stones.append(stone * 2024)
    return new_stones


if __name__ == "__main__":
    test = False
    input_data = get_input_string('11', test)
    stones = make_stones(input_data)
    ledger = defaultdict(list)
    old_map = defaultdict(int)
    for stone in stones:
        old_map[stone] += 1
    for i in range(75):
        print(i)
        new_map = defaultdict(int)
        for stone, num_stones in old_map.items():
            if stone not in ledger:
                ledger[stone] = blink(stone)
            child_stones = ledger[stone]
            for t_stone in child_stones:
                if t_stone not in new_map:
                    new_map[t_stone] = 0
                new_map[t_stone] += num_stones
            old_map = copy.deepcopy(new_map)
        total_stones = 0
        for _key, value in new_map.items():
            total_stones += value
    print(total_stones)
