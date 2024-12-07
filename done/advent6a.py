from utils import get_input_lines

from enum import Enum

class Direction(Enum):
    NORTH = '^'
    EAST = '>'
    SOUTH = 'v'
    WEST = '<'
    
    def turn_right(self):
        # Turn 90 degrees clockwise.
        rotations = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        return rotations[self]

def make_map(input_data):
    return [list(row) for row in input_data]

def locate_guard(guard_map):
    direction_chars = {
        '^': Direction.NORTH,
        '>': Direction.EAST,
        'v': Direction.SOUTH,
        '<': Direction.WEST
    }

    for i, row in enumerate(guard_map):
        for j, char in enumerate(row):
            if char in direction_chars:
                return [i, j], direction_chars[char]

def guard_on_map(guard_map):
    map_height, map_width = len(guard_map), len(guard_map[0])
    location, direction = locate_guard(guard_map)
    row, col = location

    boundary_checks = {
        Direction.NORTH: row > 0,
        Direction.EAST: col < map_width - 1,
        Direction.SOUTH: row < map_height - 1,
        Direction.WEST: col > 0
    }

    return boundary_checks[direction]

def move_guard(guard_map):
    location, direction = locate_guard(guard_map)
    row, col = location

    deltas = {
        Direction.NORTH: (-1, 0),
        Direction.EAST: (0, 1),
        Direction.SOUTH: (1, 0),
        Direction.WEST: (0, -1)
    }
    delta_row, delta_col = deltas[direction]

    next_row, next_col = row + delta_row, col + delta_col
    if guard_map[next_row][next_col] == '#':
        new_direction = direction.turn_right()
        guard_map[row][col] = new_direction.value
    else:
        guard_map[row][col] = 'X'
        guard_map[next_row][next_col] = direction.value

    keep_going = guard_on_map(guard_map)
    if not keep_going:
        final_loc, _ = locate_guard(guard_map)
        final_row, final_col = final_loc
        guard_map[final_row][final_col] = 'X'

    return keep_going

def count_visited_spots(guard_map):
    xes = 0
    for row in guard_map:
        for col in row:
            if col == 'X':
                xes += 1
    return xes

def print_map(guard_map):
    print()
    for row in guard_map:
        print(row)
    print()
    print("----------")

def execute_patrol(guard_map):
    while move_guard(guard_map):
        next


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('6', test)
    guard_map = make_map(input_data)
    execute_patrol(guard_map)
    print(count_visited_spots(guard_map))
