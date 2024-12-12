def get_input_lines(puzzle, test):
    if test:
        data_type = "test"
    else:
        data_type = "data"
    filename = f"advent{puzzle}_{data_type}.txt"
    with open(filename) as f:
        input_data = f.readlines()
    test_data = []
    for row in input_data:
        test_data.append(row.strip())
    return test_data

def get_input_string(puzzle, test):
    if test:
        data_type = "test"
    else:
        data_type = "data"
    filename = f"advent{puzzle}_{data_type}.txt"
    with open(filename) as f:
        test_data = f.read().strip()
    return test_data