
# with open('advent2_test.txt') as f:
#     test_data = f.readlines()

with open('advent2_data.txt') as f:
    test_data = f.readlines()


def make_reports(raw_data):
    input_reports = []
    for report in raw_data:
        parsed_report = report.split(' ')
        clean_data = []
        for level in parsed_report:
            clean_data.append(int(level))
        input_reports.append(clean_data)
    return input_reports

def safety_dance(report):
    if len(report) == 1:
        return True

    if report[0] == report[1]:
        return False

    ascending = report[0] < report[1]
    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1]:
            return False
        if abs(report[i] - report[i + 1]) > 3:
            return False
        if (report[i] < report[i+1]) != ascending:
            return False

    return True


if __name__ == "__main__":
    reports = make_reports(test_data)
    safe_reports = 0
    for report in reports:
        if safety_dance(report):
            safe_reports += 1
    print(safe_reports)
