def Part2(input):
    # Step 1: Parse input into grid
    # ---------------------------------------------
    #
    # Initial grid:
    # ---------------------
    # 123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +
    #
    # grid: math is written right-to-left in columns
    # ---------------------
    # + 4 431 623
    # * 175 581 32
    # + 8 248 369
    # * 356 24 1
    grid = []
    lines = input.strip().splitlines()
    n = len(lines)
    m = len(lines[0])

    # Step 2: Evaluate each row and sum results
    # -----------------------------------------------
    result_sum = 0
    for row in grid:
        operation = None
        row_result = None
        for item in row:
            # print(item)
            if isinstance(item, str):
                operation = item
            else:
                if row_result is None:  # first int
                    row_result = item
                else:
                    if operation == "*":
                        row_result *= item
                    elif operation == "+":
                        row_result += item
        if row_result is not None:
            result_sum += row_result

    return result_sum
