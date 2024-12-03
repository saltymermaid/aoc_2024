from advent2a import make_reports, safety_dance

def report_fixable(report):
    if report[0] == report[1]:
        rep_copy = report.copy()
        rep_copy.pop(0)
        return safety_dance(rep_copy)

    ascending = report[0] < report[1]
    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1]:
            r_copy = report.copy()
            r_copy.pop(i)
            return safety_dance(r_copy)
        if (abs(report[i] - report[i + 1]) > 3) or ((report[i] < report[i+1]) != ascending):
            a_copy = report.copy()
            a_copy.pop(i)
            if safety_dance(a_copy):
                return True
            b_copy = report.copy()
            b_copy.pop(i + 1)
            if safety_dance(b_copy):
                return True
        return check_all(report)
    return False


def check_all(report):
    for i in range(len(report)):
        missing_one_report = report[:i] + report[i + 1:]
        if safety_dance(missing_one_report):
            return True
    return False


if __name__ == "__main__":

    test = False
    if test:
        data_filename = 'advent2_test.txt'
    else:
        data_filename = 'advent2_data.txt'

    with open(data_filename) as f:
        test_data = f.readlines()
    reports = make_reports(test_data)
    safe_reports = 0
    for report in reports:
        if safety_dance(report) or report_fixable(report):
            safe_reports += 1
    print(safe_reports)
