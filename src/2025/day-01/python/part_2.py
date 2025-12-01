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


def Part2(input):
    password, count = 50, 0
    for line in input.strip().splitlines():
        direction, rotation = line[0], int(line[1:])
        rotation = rotation if direction == "R" else -rotation

        new_password = password + rotation

        # detect positive to negative crossing on a left turn
        if direction == "L" and password > 0 > new_password:
            count += 1

        password = new_password
        count += (abs(password) // 100) or (1 if password == 0 else 0)
        password %= 100

    return count
