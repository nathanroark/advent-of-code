def Part2(input):
    ranges = []

    # Parse all ranges
    # -------------------------------------------------
    for line in input.strip().splitlines():
        if line == "":
            break
        r1, r2 = line.split("-")
        ranges.append([int(r1), int(r2)])

    # Sort then so we extend them easily
    ranges.sort()

    # Merge overlapping/adjacent ranges
    # -------------------------------------------------
    merged = [ranges[0]]
    for current in ranges[1:]:
        # If current overlaps or is adjacent to last, merge them
        if current[0] <= merged[-1][1] + 1:  # +1 to connect adjacent ranges
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)

    # Count coverage
    # -------------------------------------------------
    count = 0
    for r in merged:
        count += r[1] - r[0] + 1

    return count
