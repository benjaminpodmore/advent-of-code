import argparse
from pathlib import Path

def get_data(path: Path):
    data = []
    with open(path, "r") as f:
        data = [line.strip() for line in f.readlines()]
    return data 


def solve(data: list[str]):
    res = 0
    for bank in data:
        max_val = compute_fast(bank, 2)
        res += max_val
    return res 

def compute_slow(bank: str) -> int:
    max_val = -1
    for i in range(len(bank) - 1):
        for j in range(i+1, len(bank)):
            val = int(bank[i]+bank[j])
            max_val = max(max_val, val)
    return max_val 

def compute_fast(bank: str, digit_len: int) -> int:
    digits = []

    max_val = -1
    return max_val


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        filename = "test_input"
    else:
        filename = "input"
    script_dir = Path(__file__).parent
    path = script_dir / filename
    data = get_data(path)
    res = solve(data)
    print(res)
