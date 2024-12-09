from itertools import combinations
from utils import get_input_lines
from advent8a import make_map, print_map, count_antinodes

def add_antinodes(antennas, antenna_map):
    grid_height, grid_width = len(antenna_map), len(antenna_map[0])

    def is_in_bounds(x: int, y: int) -> bool:
        return 0 <= x < grid_height and 0 <= y < grid_width

    def set_antinode(x: int, y: int):
        if is_in_bounds(x, y):
            antenna_map[x][y].antinode = True

    for locations in antennas.values():
        if len(locations) == 1:
            next
        for first_pos, second_pos in combinations(locations, 2):
            first_node = antenna_map[first_pos[0]][first_pos[1]]
            second_node = antenna_map[second_pos[0]][second_pos[1]]
            first_node.antinode = True
            second_node.antinode = True

            x_offset, y_offset = first_node.distance_between(second_node)

            first_x = first_node.row + x_offset
            first_y = first_node.col + y_offset
            while(is_in_bounds(first_x, first_y)):
                set_antinode(first_x, first_y)
                first_x += x_offset
                first_y += y_offset

            second_x = second_node.row - x_offset
            second_y = second_node.col - y_offset
            while(is_in_bounds(second_x, second_y)):
                set_antinode(second_x, second_y)
                second_x -= x_offset
                second_y -= y_offset

    return antenna_map

if __name__ == "__main__":
    test = False
    input_data = get_input_lines('8', test)
    antenna_map, antennas = make_map(input_data)
    map_with_antinodes = (add_antinodes(antennas, antenna_map))
    print(count_antinodes(map_with_antinodes))
