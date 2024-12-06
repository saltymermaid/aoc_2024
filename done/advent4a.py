from utils import get_input_lines

def create_grid(raw_data):
    grid = [list(line.strip()) for line in raw_data]
    return grid

def find_christmas(candidate):
    return "".join(candidate).count('XMAS')

def get_all_groups(grid):
    width = len(grid[0])
    height = len(grid)
    groups = []
    groups.extend(grid + [row[::-1] for row in grid])
    columns = list(zip(*grid))
    groups.extend(columns + [col[::-1] for col in columns])
    for direction in [True, False]:
        # Top row
        for i in range(width):
            diag = get_diag(0, i, grid, direction)
            groups.extend([diag, diag[::-1]])
        
        # Left/right column (skip first row as it's covered)
        start_col = 0 if direction else width - 1
        for i in range(1, height):
            diag = get_diag(i, start_col, grid, direction)
            groups.extend([diag, diag[::-1]])
    return groups

def get_diag(row, col, grid, right = True):
    height, width = len(grid), len(grid[0])
    diag = []
    while 0 <= row < height and 0 <= col < width:
        diag.append(grid[row][col])
        row += 1
        col = col + 1 if right else col - 1
    return diag

if __name__ == "__main__":
    test = False
    test_data = get_input_lines(4, test)
    clean_data = create_grid(test_data)
    xmas_groups = get_all_groups(clean_data)
    xmases = 0
    for group in xmas_groups:
        xmases += find_christmas(group)
    print(xmases)
