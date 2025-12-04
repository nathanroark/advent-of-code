# find largest number that can be formed by selecting 12 digits from each line of input
# digits must come out of the line in order
def Part2(input):
    digits = 12
    sum = 0
    for d in input.strip().split("\n"):
        n = len(d)
        dp = [[-1] * (digits + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            digit = int(d[i - 1])
            for j in range(digits + 1):
                # Not take the current digit
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # Take the current digit
                if j > 0 and dp[i - 1][j - 1] != -1:
                    value = dp[i - 1][j - 1] * 10 + digit
                    dp[i][j] = max(dp[i][j], value)

        max_digit = dp[n][digits]
        sum += max_digit
    return sum
