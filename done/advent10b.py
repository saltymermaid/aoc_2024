from dataclasses import dataclass, field
from typing import Set, Tuple
from utils import get_input_lines
from advent10a import create_map

def find_trails(current_location, trail_score, topo_map, trail_head):
    if current_location.elevation == 9:
        trail_score += 1
        return trail_score
    next_neighbor = current_location.can_go_up(topo_map)
    if next_neighbor:
        trail_score = find_trails(next_neighbor, trail_score, topo_map, trail_head)
    next_neighbor = current_location.can_go_right(topo_map)
    if next_neighbor:
        trail_score = find_trails(next_neighbor, trail_score, topo_map, trail_head)
    next_neighbor = current_location.can_go_down(topo_map)
    if next_neighbor:
        trail_score = find_trails(next_neighbor, trail_score, topo_map, trail_head)
    next_neighbor = current_location.can_go_left(topo_map)
    if next_neighbor:
        trail_score = find_trails(next_neighbor, trail_score, topo_map, trail_head)
    return trail_score

def find_all_trails(topo_map):
    all_trail_scores = 0
    num_trailheads = 0
    for row in topo_map:
        for col in row:
            if col.is_trailhead():
                num_trailheads += 1
                this_trail_score = find_trails(col, 0, topo_map, col)
                all_trail_scores += this_trail_score
    return all_trail_scores


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('10', test)
    topo_map = create_map(input_data)
    total_score = find_all_trails(topo_map)
    print(total_score)
