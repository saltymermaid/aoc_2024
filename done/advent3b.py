import re
from utils import get_input_string
from advent3a import multiply_pairs

def clean_memory(corrupt_instructions):
    pattern = r"mul\((\d+),(\d+)\)"
    pairs = []
    candidates = corrupt_instructions.split("don't")
    chunks = [candidates.pop(0)]
    for candidate in candidates:
        do_split = candidate.split("do")
        chunks += do_split[1:]
    for do_chunk in chunks:
        pairs += re.findall(pattern, do_chunk)
    return pairs

if __name__ == "__main__":
    test = False
    test_data = get_input_string(3, test)
    good_instructions = clean_memory(test_data)
    executed_instructions = multiply_pairs(good_instructions)
    all_instructions = sum(executed_instructions)
    print(all_instructions)