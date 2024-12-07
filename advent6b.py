from dataclasses import dataclass
from typing import Optional
from enum import Enum, auto
import copy
from utils import get_input_lines
from advent6a import Direction

guard_state = {
    'position': None,
    'direction': None
}

@dataclass
class Cell:
    current_state: str
    path_marker: str = '.'
    last_direction: Optional[Direction] = None

    def mark_path(self, direction: Direction) -> None:
        if direction in (Direction.NORTH, Direction.SOUTH):
            new_marker = '|'
        else:
            new_marker = '-'

        if self.path_marker in (new_marker, '.'):
            self.path_marker = new_marker
        else:
            self.path_marker = '+'

        self.last_direction = direction

    def is_obstacle(self) -> bool:
        return self.current_state in ('#', 'O')

def make_map(input_data):
    direction_chars = {
        '^': Direction.NORTH,
        '>': Direction.EAST,
        'v': Direction.SOUTH,
        '<': Direction.WEST
    }

    guard_map = []
    for row_idx, row in enumerate(input_data):
        map_row = []
        for col_idx, char in enumerate(row):
            cell = Cell(current_state=char)
            # check for guard and update guard state
            if char in direction_chars:
                guard_state['position'] = [row_idx, col_idx]
                guard_state['direction'] = direction_chars[char]
                cell.path_marker = '|'
                cell.last_direction = Direction.NORTH
            map_row.append(cell)
        guard_map.append(map_row)

    return guard_map

def guard_on_map(guard_map):
    map_height, map_width = len(guard_map), len(guard_map[0])
    row, col = guard_state['position']
    direction = guard_state['direction']

    boundary_checks = {
        Direction.NORTH: row > 0,
        Direction.EAST: col < map_width - 1,
        Direction.SOUTH: row < map_height - 1,
        Direction.WEST: col > 0
    }

    return boundary_checks[direction]

from enum import Enum, auto

class PatrolState(Enum):
    CONTINUE = auto()
    LOOP_DETECTED = auto()
    COMPLETE = auto()

def move_guard(guard_map):
    if not guard_on_map(guard_map):
        return PatrolState.COMPLETE

    row, col = guard_state['position']
    direction = guard_state['direction']
    deltas = {
        Direction.NORTH: (-1, 0),
        Direction.EAST: (0, 1),
        Direction.SOUTH: (1, 0),
        Direction.WEST: (0, -1)
    }
    next_row = row + deltas[direction][0]
    next_col = col + deltas[direction][1]

    direction_symbol = "|" if direction in [Direction.NORTH, Direction.SOUTH] else "-"
    marked_symbol = direction_symbol if guard_map[row][col].path_marker in [direction_symbol, "."] else "+"
    if guard_map[next_row][next_col].is_obstacle():
        new_direction = direction.turn_right()
        guard_map[row][col].current_state = new_direction.value
        guard_map[row][col].path_marker = "+"
        guard_state['direction'] = new_direction
    else:
        guard_map[row][col].current_state = marked_symbol
        guard_map[row][col].path_marker = marked_symbol
        guard_map[next_row][next_col].current_state = direction.value
        guard_state['position'] = [next_row, next_col]
        if guard_on_map(guard_map):
            guard_map[next_row][next_col].last_direction = direction

    if guard_in_loop(guard_map):
        return PatrolState.LOOP_DETECTED
    elif not guard_on_map(guard_map):
        return PatrolState.COMPLETE

    return PatrolState.CONTINUE

def guard_in_loop(guard_map):
    if not guard_on_map(guard_map):
        return False
    
    row, col = guard_state['position']
    direction = guard_state['direction']

    deltas = {
        Direction.NORTH: (-1, 0),
        Direction.EAST: (0, 1),
        Direction.SOUTH: (1, 0),
        Direction.WEST: (0, -1)
    }
    delta_row, delta_col = deltas[direction]

    next_row, next_col = row + delta_row, col + delta_col
    next_spot = guard_map[next_row][next_col].last_direction
    if direction == next_spot:
        return True
    return False

def execute_patrol(guard_map):
    state = PatrolState.CONTINUE
    while state == PatrolState.CONTINUE:
        state = move_guard(guard_map)
    return state

def print_map(guard_map):
    print()
    for row in guard_map:
        for spot in row:
            print(spot.current_state, end=" ")
        print("")
    print()
    print("----------")

if __name__ == "__main__":
    test = True
    input_data = get_input_lines('6', test)
    rows, cols = len(input_data), len(input_data[0])
    obstacles = 0
    base_map = make_map(input_data)
    initial_guard_state = guard_state.copy()

    for row in range(rows):
        for col in range(cols):
            if not test:
                print(f"{row} : {col}")
            if input_data[row][col] == ".":
                guard_state.update(initial_guard_state)
                guard_map = copy.deepcopy(base_map)
                guard_map[row][col].current_state = "O"
                guard_map[row][col].path_marker = "O"

                result = execute_patrol(guard_map)
                if result == PatrolState.LOOP_DETECTED:
                    obstacles += 1
    print(f"Obstacles: {obstacles}")