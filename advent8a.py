from dataclasses import dataclass
from typing import Optional
from collections import defaultdict
from itertools import combinations
from utils import get_input_lines

@dataclass
class Node:
    antenna: str
    row: int
    col: int
    antinode: Optional[bool] = False

    def distance_between(self, other_node):
        x_distance = self.row - other_node.row
        y_distance = self.col - other_node.col
        return x_distance, y_distance

def make_map(input_data):
    grid = []
    antennas = defaultdict(list)
    for row_idx, row in enumerate(input_data):
        map_row = []
        for col_idx, char in enumerate(row):
            position = (row_idx, col_idx)
            node = Node(antenna = char, row = row_idx, col = col_idx)
            map_row.append(node)
            if char != ".":
                antennas[char].append(position)
        grid.append(map_row)
    return grid, antennas

def count_antinodes(antenna_map):
    return sum(node.antinode for row in antenna_map for node in row)

def print_map(map):
    for row in map:
        for char in row:
            if char.antinode and char.antenna == ".":
                print("#", end = " ")
            else:
                print(char.antenna, end= " ")
        print("")
    print("---------------")

def add_antinodes(antennas, antenna_map):
    grid_height, grid_width = len(antenna_map), len(antenna_map[0])

    def is_in_bounds(x, y):
        return 0 <= x < grid_height and 0 <= y < grid_width

    def set_antinode(x, y):
        if is_in_bounds(x, y):
            antenna_map[x][y].antinode = True

    for locations in antennas.values():
        for first_pos, second_pos in combinations(locations, 2):
            first_node = antenna_map[first_pos[0]][first_pos[1]]
            second_node = antenna_map[second_pos[0]][second_pos[1]]

            x_offset, y_offset = first_node.distance_between(second_node)

            first_x = first_node.row + x_offset
            first_y = first_node.col + y_offset
            set_antinode(first_x, first_y)

            second_x = second_node.row - x_offset
            second_y = second_node.col - y_offset
            set_antinode(second_x, second_y)

    return antenna_map

if __name__ == "__main__":
    test = True
    input_data = get_input_lines('8', test)
    antenna_map, antennas = make_map(input_data)
    map_with_antinodes = (add_antinodes(antennas, antenna_map))
    print(count_antinodes(map_with_antinodes))
