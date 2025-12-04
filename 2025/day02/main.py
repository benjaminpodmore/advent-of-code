from pathlib import Path
import math

def get_data(path: Path):
    data = []
    with open(path, "r") as f:
        line = f.readline()
        ranges = line.split(",")
        for r in ranges:
            data.append(tuple(r.strip().split("-")))
    return data 


def solve(data: list[tuple[int, int]]):
    res = 0
    for r in data:
        for i in range(int(r[0]),int(r[1]) + 1):
            if check(str(i)):
              res += i
    return res 

def check(num: str):
    double_string = num + num
    string_to_check = double_string[1:len(double_string)-1]
    if num in string_to_check:
        return True
    return False



if __name__ == "__main__":
    filename = "input"
    script_dir = Path(__file__).parent
    path = script_dir / filename
    data = get_data(path)
    res = solve(data)
    print(res)
