from dataclasses import dataclass, field
from typing import Set, Tuple
from utils import get_input_lines

@dataclass
class TrailSpot:
    elevation: int
    x: int
    y: int
    peaks: Set[Tuple[int, int]] = field(default_factory=set)

    def is_trailhead(self):
        return self.elevation == 0

    def can_go_up(self, topo_map):
        if self.y == 0:
            return None
        else:
            neighbor = topo_map[self.y - 1][self.x]
            if neighbor.elevation == self.elevation + 1:
                return neighbor

    def can_go_right(self, topo_map):
        if self.x == len(topo_map[0]) - 1:
            return None
        else:
            neighbor = topo_map[self.y][self.x + 1]
            if neighbor.elevation == self.elevation + 1:
                return neighbor

    def can_go_down(self, topo_map):
        if self.y == len(topo_map) - 1:
            return None
        else:
            neighbor = topo_map[self.y + 1][self.x]
            if neighbor.elevation == self.elevation + 1:
                return neighbor

    def can_go_left(self, topo_map):
        if self.x == 0:
            return None
        else:
            neighbor = topo_map[self.y][self.x - 1]
            if neighbor.elevation == self.elevation + 1:
                return neighbor

def create_map(input_data):
    return [
        [TrailSpot(int(col), col_idx, row_idx) 
         for col_idx, col in enumerate(row)]
        for row_idx, row in enumerate(input_data)
    ]

def print_map(topo_map):
    for row in topo_map:
        for col in row:
            print(col.elevation, end = "")
        print("")

def find_trails(current_location, trail_score, topo_map, trail_head):
    if current_location.elevation == 9:
        this_peak = (current_location.x, current_location.y)
        if this_peak not in trail_head.peaks:
            trail_score += 1
        trail_head.peaks.add(this_peak)
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
