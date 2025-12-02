import textwrap


def Part2(input):
    data = input.strip().split(",")
    sum = 0
    for d in data:
        id = d.split("-")
        first_id, last_id = int(id[0]), int(id[1])
        for num in range(first_id, last_id + 1):
            num_str = str(num)

            n = len(num_str)

            for m in range(1, (n // 2) + 1):
                # q: quotent, r: remainder
                _, r = divmod(n, m)

                # check for even split
                if r != 0:
                    continue

                num_strs = textwrap.wrap(num_str, m)

                if not all(x == num_strs[0] for x in num_strs):
                    continue

                sum += num
                break

    return sum
