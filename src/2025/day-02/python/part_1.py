def Part1(input):
    data = input.strip().split(",")
    sum = 0
    for d in data:
        id = d.split("-")
        first_id, last_id = int(id[0]), int(id[1])
        for n in range(first_id, last_id + 1):
            s = str(n)

            # q: quotent, r: remainder
            q, r = divmod(len(s), 2)

            if r != 0:
                continue

            first, second = s[: q + r], s[q + r :]

            if first != second:
                continue

            sum += n

    return sum
