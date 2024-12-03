
with open('advent1_data.txt') as f:
    test_data = f.readlines()


def make_lists(raw_data):
    list_a = []
    list_b = []
    for pair in raw_data:
        nums_raw = pair.split("   ")
        list_a.append(int(nums_raw[0]))
        list_b.append(int(nums_raw[1]))
    list_a.sort()
    list_b.sort()
    return list_a, list_b

def get_pairs(left, right):
    paired_nums = []
    for l, r in zip(left, right):
        paired_nums.append([l, r])
    return paired_nums


if __name__ == "__main__":
    left_list, right_list = make_lists(test_data)
    pairs = get_pairs(left_list, right_list)
    total_distance = 0
    for pair in pairs:
        distance = abs(pair[0] - pair[1])
        total_distance += distance
    print(total_distance)