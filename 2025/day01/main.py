import os

def get_input(path: str):
    with open(path, "r") as f:
        lines = f.readlines()

    return lines

def solve(rotations: list[str], dial_reset: int = 100):
    pos = 50
    zero_passes = 0
    for rotation in rotations:
        direction = rotation[0]
        number = int(rotation[1:])
        full_turns = number // dial_reset
        net_turns = number % dial_reset
        old_pos = pos
        if net_turns == 0:
            zero_passes += full_turns
            continue
        if direction == "L":
            pos -= net_turns
            if pos <= 0:
                pos = dial_reset + pos
                if old_pos > 0:
                    zero_passes += 1
        elif direction == "R":
            pos += net_turns
            if pos >= dial_reset:
                pos = pos - dial_reset
                if old_pos < dial_reset:
                    zero_passes += 1
        zero_passes += full_turns
        print(direction, number, pos, zero_passes)
    return pos, zero_passes

if __name__ == "__main__":
    filename = "input"
    script_path = os.path.abspath(__file__)
    directory_path = os.path.dirname(script_path)
    path = os.path.join(directory_path, filename)
    input = get_input(path)

    pos, zero_passes = solve(input)
    print(zero_passes)
