from dataclasses import dataclass
from utils import get_input_lines

@dataclass
class Robot:
    p_x: int
    p_y: int
    v_x: int
    v_y: int

    def move(self, width, height):
        self.p_x = (self.p_x + self.v_x) % width
        self.p_y = (self.p_y + self.v_y) % height

def generate_robots(input_data):
    robots = []
    for row in input_data:
        raw_pos, raw_vel = row.split(" ")
        px, py = raw_pos[2:].split(",")
        vx, vy = raw_vel[2:].split(",")
        robots.append(Robot(int(px), int(py), int(vx), int(vy)))
    return robots

def move_robot(robot, width, height, iterations = 100, ):
    for _i in range(iterations):
        robot.move(width, height)

def count_robots(robots, height, width):
    upper_left = 0
    upper_right = 0
    lower_left = 0
    lower_right = 0
    center_h = width // 2
    center_v = height // 2
    for robot in robots:
        if robot.p_x < center_h:
            if robot.p_y < center_v:
                upper_left += 1
            elif robot.p_y > center_v:
                lower_left += 1
        elif robot.p_x > center_h:
            if robot.p_y < center_v:
                upper_right += 1
            elif robot.p_y > center_v:
                lower_right += 1
    return upper_left * upper_right * lower_left * lower_right

def print_robots(robots, height, width):
    robot_map = []
    for row in range(height):
        robot_map_row = []
        for col in range(width):
            robot_map_row.append(0)
        robot_map.append(robot_map_row)
    for robot in robots:
        robot_map[robot.p_y][robot.p_x] += 1
    for row in robot_map:
        for col in row:
            if col == 0:
                print(".", end = "")
            else:
                print(col, end = "")
        print("")


if __name__ == "__main__":
    test = True
    if test:
        height = 7
        width = 11
    else:
        height = 103
        width = 101
    input_data = get_input_lines('14', test)
    robots = generate_robots(input_data)
    for robot in robots:
        move_robot(robot, width, height, 100)
    # print_robots(robots, height, width)
    print(count_robots(robots, height, width))
