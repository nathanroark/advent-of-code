def Part1(input):
    password, count = 50, 0
    for line in input.strip().splitlines():
        direction, rotation = line[0], int(line[1:])
        rotation = rotation if direction == "R" else -rotation

        password = (password + rotation) % 100

        # print(f"The dial is rotated {line} to point at {fancy(password)}.")

        count += 1 if password == 0 else 0

    return count
