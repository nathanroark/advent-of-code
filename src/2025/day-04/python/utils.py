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
