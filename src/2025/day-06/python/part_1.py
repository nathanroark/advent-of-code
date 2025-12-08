def Part1(input):
    # Ranges (e.g.: (3, 5), (10, 18))
    fresh_ranges: list[list[int]] = []
    lines = input.strip().splitlines()
    i = 0

    # Build ranges
    # ---------------------------
    while True:
        r1, r2 = lines[i].split("-")
        r1, r2 = int(r1), int(r2)
        extended = False
        for fresh in fresh_ranges:
            # option 1: extend lower bound
            if r1 <= fresh[0] and r2 >= fresh[0] and r2 <= fresh[1]:
                fresh[0] = r1
                extended = True

            # option 2: extend upper bound
            if r2 >= fresh[1] and r1 >= fresh[0] and r1 <= fresh[1]:
                fresh[1] = r2
                extended = True

        # option 3: add unique range
        if not extended:
            fresh_ranges.append([int(r1), int(r2)])

        i += 1
        if lines[i] == "":
            break

    i += 1

    # Check freshness
    # ---------------------------
    count = 0
    for j in range(i, len(lines)):
        for fresh in fresh_ranges:
            if int(lines[j]) >= fresh[0] and int(lines[j]) <= fresh[1]:
                count += 1
                break

    return count
