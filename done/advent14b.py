import math
from utils import get_input_lines
from advent14a import Robot, generate_robots, move_robot, count_robots, print_robots


if __name__ == "__main__":
    test = False
    if test:
        height = 7
        width = 11
    else:
        height = 103
        width = 101
    input_data = get_input_lines('14', test)
    robots = generate_robots(input_data)
    robot_count = math.inf
    best_second = 0
    for second in range(10000):
        for robot in robots:
            move_robot(robot, width, height, 1)
        robot_count = min(robot_count, count_robots(robots, height, width))
        if count_robots(robots, height, width) == robot_count:
            best_second = second
    print(best_second + 1)
