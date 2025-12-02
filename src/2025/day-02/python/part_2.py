import textwrap


def Part2(input):
    data = input.strip().split(",")
    sum = 0
    for d in data:
        id = d.split("-")
        first_id, last_id = int(id[0]), int(id[1])
        for num in range(first_id, last_id + 1):
            num_string = str(num)

            n = len(num_string)

            for m in range(1, n):
                # q: quotent, r: remainder
                _, r = divmod(n, m)

                # check for even split
                if r != 0:
                    continue

                nums = textwrap.wrap(num_string, m)

                if not all(x == nums[0] for x in nums):
                    continue

                sum += num
                break

    return sum
