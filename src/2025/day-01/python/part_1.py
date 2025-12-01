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
    password = 50
    count = 0
    lines = input.strip().split("\n")
    for line in lines:
        direction = line[0]
        rotation = int(line[1:])
        if direction == "L":
            rotation *= -1

        password = (password + rotation) % 100

        # print(f"The dial is rotated {line} to point at {fancy(password)}.")

        if password == 0:
            count += 1

    return count
