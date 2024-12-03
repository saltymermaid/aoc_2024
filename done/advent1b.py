from advent1a import make_lists, get_pairs

with open('advent1_data.txt') as f:
    test_data = f.readlines()

def count_nums(right_list):
    num_dict = {}
    for num in right_list:
        if num not in num_dict:
            num_dict[num] = 0
        num_dict[num] += 1
    return num_dict


if __name__ == "__main__":
    left_list, right_list = make_lists(test_data)
    right_num_dict = count_nums(right_list)
    total_similarity = 0
    for num in left_list:
        if num in right_num_dict:
            total_similarity += num * right_num_dict[num]
    print(total_similarity)