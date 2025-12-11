import argparse
from pathlib import Path

steps = [(x,y) for x in (1, 0, -1) for y in (1,0, -1) if not (x == 0 and y == 0)]

def get_data(path: Path) -> list[list[str]]:
    data = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(list(line.strip()))
    return data

def solve(grid: list[list[str]]) -> int:
    count = 0
    grid_copy = grid
    are_rolls_remaining = True
    while are_rolls_remaining:
        res, indices = solve_grid(grid_copy)
        for index in indices:
            i = index[0]
            j = index[1]
            grid_copy[i][j] = "."
        count += res
        if res == 0:
            are_rolls_remaining = False
    return count


def solve_grid(grid: list[list[str]]) -> tuple[int, list[tuple[int, int]]]:
    spot_count = 0
    indices = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue
            count = 0 
            for step in steps:
                x = i + step[0]
                y = j + step[1]
                if x < 0 or x >= len(grid):
                    continue
                if y < 0 or y >= len(grid[0]):
                    continue
                if grid[x][y] == "@":
                    count += 1
            if count < 4:
                spot_count += 1
                indices_to_remove = (i, j)
                indices.append(indices_to_remove)

    return spot_count, indices

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")

    args = parser.parse_args()
    if args.test:
        filename = "test_input"
    else:
        filename = "input"
    parent_dir = Path(__file__).parent
    path = parent_dir / filename
    data = get_data(path)
    
    res = solve(data)
    print(res)
