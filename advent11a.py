from utils import get_input_string

def make_stones(input_data):
    return input_data.split(" ")

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            num_digits = len(stone)
            half = num_digits // 2
            new_stones.extend([str(int(stone[:half])), str(int(stone[half:]))])
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones


if __name__ == "__main__":
    test = False
    input_data = get_input_string('11', test)
    stones = make_stones(input_data)
    for i in range(25):
        stones = blink(stones)
    print(len(stones))
