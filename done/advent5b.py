from utils import get_input_lines
from advent5a import get_rules, get_updates, get_middle_update, check_updates

def fix_updates(updates, all_rules):
    for i, page in enumerate(updates):
        must_precede = all_rules.get(page, [])

        for j, update in enumerate(updates[i:]):
            if update in must_precede:
                fixed = [
                    *updates[:i],
                    update,
                    *updates[i:j + i],
                    *updates[j + i + 1:]
                ]

                if check_updates(fixed, all_rules):
                    return fixed

                return fix_updates(fixed, all_rules)

    return updates


if __name__ == "__main__":
    test = False
    raw_rules = get_input_lines('5r', test)
    pre_rules = get_rules(raw_rules)
    raw_updates = get_input_lines('5u', test)
    updates = get_updates(raw_updates)
    
    total_middles = sum(
        int(get_middle_update(fix_updates(update, pre_rules)))
        for update in updates
        if not check_updates(update, pre_rules)
    )
    print(total_middles)
