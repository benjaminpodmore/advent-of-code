from pathlib import Path
import argparse

def get_data(path: Path) -> tuple[list[tuple[int, int]],list[int]]:
    ranges = []
    ingredients = []

    with open(path, "r") as f:
        lines = f.readlines()
        finished_ranges = False
        for line in lines:
            if line.strip() == "":
                finished_ranges = True
                continue
            if not finished_ranges:
                curr_range = line.strip().split("-")
                ranges.append(curr_range)
            else:
                ingredients.append(line.strip())

    return  ranges, ingredients

def solve(ranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    range_set = set()
    res = 0
    print("Reading ranges")
    for ingredient_range in ranges:
        for i in range(int(ingredient_range[0]),int(ingredient_range[1]) + 1):
            range_set.add(i)

    print("Processing ingredients")
    for ingredient in ingredients:
        if int(ingredient) in range_set:
            res += 1

    return res

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
    print("Reading data...")

    ranges, ingredients = get_data(path)
    res = solve(ranges, ingredients)
    print(res)

