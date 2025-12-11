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
        max_val = compute_fast(bank, 12)
        res += max_val
    return res 

def compute_slow(bank: str) -> int:
    max_val = -1
    for i in range(len(bank) - 1):
        for j in range(i+1, len(bank)):
            val = int(bank[i]+bank[j])
            max_val = max(max_val, val)
    return max_val 

def find_max(bank: str, start: int, end: int) -> tuple[int, str]:
    max_val_index = -1
    max_val = "-1"
    for idx, digit in enumerate(bank[start:end]):
        if int(digit) > int(max_val):
            max_val = digit
            max_val_index = idx

    return max_val_index + start, max_val

def compute_fast(bank: str, num_digits: int) -> int:
    digits: list[str] = []
    count = 0

    start = 0
    end = len(bank) - num_digits + 1
    while count < num_digits:
        first_digit_index, digit = find_max(bank, start, end)
        count += 1
        start = first_digit_index + 1
        end = len(bank) - num_digits + count + 1
        digits.append(digit)

    return int("".join(digits))


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
