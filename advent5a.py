from utils import get_input_lines

from collections import defaultdict

def get_rules(raw_data):
    rules = defaultdict(list)
    for row in raw_data:
        before, after = row.split("|")
        rules[after].append(before)
    return rules

def get_updates(raw_data):
    return [row.split(",") for row in raw_data]

def get_middle_update(updates):
    return updates[len(updates) // 2]

def check_updates(updates, all_rules):
    for i, page in enumerate(updates):
        must_precede = []
        if page in all_rules:
            # set the rules
            must_precede = all_rules[page]
        for update in updates[i:]:
            if update in must_precede:
                return False
    return True


if __name__ == "__main__":
    test = False
    raw_rules = get_input_lines('5r', test)
    rules = get_rules(raw_rules)
    raw_updates = get_input_lines('5u', test)
    updates = get_updates(raw_updates)
    total_middles = sum(int(get_middle_update(update)) 
                       for update in updates 
                       if check_updates(update, rules))
    print(total_middles)
