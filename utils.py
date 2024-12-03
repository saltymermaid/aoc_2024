def get_input_lines(puzzle, test):
    if test:
        data_type = "test"
    else:
        data_type = "data"
    filename = f"advent{puzzle}_{data_type}.txt"
    with open(filename) as f:
        test_data = f.readlines()
    return test_data

def get_input_string(puzzle, test):
    if test:
        data_type = "test"
    else:
        data_type = "data"
    filename = f"advent{puzzle}_{data_type}.txt"
    with open(filename) as f:
        test_data = f.read()
    return test_data