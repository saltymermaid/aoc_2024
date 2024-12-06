import re
from utils import get_input_lines
from advent4a import create_grid

def find_mas(candidate):
    pattern = "[M][A-Z][M][A-Z]A[A-Z][S][A-Z][S]|[M][A-Z][S][A-Z]A[A-Z][M][A-Z][S]|[S][A-Z][S][A-Z]A[A-Z][M][A-Z][M]|[S][A-Z][M][A-Z]A[A-Z][S][A-Z][M]"
    puzzle_string = "".join(candidate)
    return bool(re.search(pattern, puzzle_string))

def get_all_groups(grid):
    width = len(grid[0])
    return [grid[y][x:x+3] + grid[y+1][x:x+3] + grid[y+2][x:x+3]
            for y in range(width - 2)
            for x in range(width - 2)]

if __name__ == "__main__":
    test = False
    test_data = get_input_lines(4, test)
    clean_data = create_grid(test_data)
    xmas_groups = get_all_groups(clean_data)
    print(sum(find_mas(group) for group in xmas_groups))
