from dataclasses import dataclass
from utils import get_input_lines

@dataclass
class Plot:
    crop: str
    fences: int
    x: int
    y: int
    region: int
    visited: bool

    def top_neighbor(self, garden):
        if self.y == 0:
            return None
        return garden[self.y - 1][self.x]

    def right_neighbor(self, garden):
        garden_width = len(garden[0]) - 1
        if self.x == garden_width:
            return None
        return garden[self.y][self.x + 1]

    def bottom_neighbor(self, garden):
        garden_height = len(garden) - 1
        if self.y == garden_height:
            return None
        return garden[self.y + 1][self.x]

    def left_neighbor(self, garden):
        if self.x == 0:
            return None
        return garden[self.y][self.x - 1]

    def set_fences(self, garden):
        for direction in [self.top_neighbor, self.right_neighbor, self.bottom_neighbor, self.left_neighbor]:
            neighbor = direction(garden)
            if neighbor:
                self.fences += neighbor.crop != self.crop
            else:
                self.fences += 1

def create_garden(input_data):
    return [[Plot(col, 0, col_idx, row_idx, -1, False) for col_idx, col in enumerate(row)] for row_idx, row in enumerate(input_data)]

def calculate_fences(garden):
    for row in garden:
        for plot in row:
            plot.set_fences(garden)

def print_garden(garden, attribute):
    for row in garden:
        for plot in row:
            value = getattr(plot, attribute)
            print(value, end = "")
        print("")
    print("----------")

def add_neighbors(plot, garden, fence_count):
    for direction in [plot.top_neighbor, plot.right_neighbor, plot.bottom_neighbor, plot.left_neighbor]:
        neighbor = direction(garden)
        if neighbor and neighbor.crop == plot.crop and not neighbor.visited:
            neighbor.visited = True
            neighbor.region = plot.region
            fence_count.append(neighbor.fences)
            garden, fence_count = add_neighbors(neighbor, garden, fence_count)
    return garden, fence_count

def map_regions(garden):
    region_id = 0
    total_fence_cost = 0
    for row_idx, row in enumerate(garden):
        for plot_idx, plot in enumerate(row):
            if plot.region >= 0:
                next
            else:
                garden[row_idx][plot_idx].region = region_id
                region_fence_list = [garden[row_idx][plot_idx].fences]
                garden[row_idx][plot_idx].visited = True
                garden, region_fence_list = add_neighbors(garden[row_idx][plot_idx], garden, region_fence_list)
                total_fence_cost += len(region_fence_list) * sum(region_fence_list)
                region_id += 1
    return garden, total_fence_cost


if __name__ == "__main__":
    test = False
    input_data = get_input_lines('12', test)
    garden = create_garden(input_data)
    calculate_fences(garden)
    garden, fences = map_regions(garden)
    print(fences)
