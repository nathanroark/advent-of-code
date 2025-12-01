class c:
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    BLUE = "\033[94m"
    PINK = "\033[95m"
    CYAN = "\033[96m"


def fancy(value):
    if value == 0:
        value = f"{c.RED}{value}{c.ENDC}"
    else:
        value = f"{c.ORANGE}{value}{c.ENDC}"
    return value


def Part1(input):
    password, count = 50, 0
    for line in input.strip().splitlines():
        direction, rotation = line[0], int(line[1:])
        rotation = rotation if direction == "R" else -rotation

        password = (password + rotation) % 100

        # print(f"The dial is rotated {line} to point at {fancy(password)}.")

        count += 1 if password == 0 else 0

    return count
