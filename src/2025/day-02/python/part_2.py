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
