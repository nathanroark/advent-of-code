# brute force solution for day 3 part 1
def Part1(input):
    sum = 0

    for d in input.strip().split("\n"):
        max_digit = -1
        for i in range(len(d)):
            first = int(d[i]) * 10
            for j in range(i + 1, len(d)):
                second = int(d[j])
                if first + second > max_digit:
                    max_digit = first + second
        sum += max_digit

    return sum
