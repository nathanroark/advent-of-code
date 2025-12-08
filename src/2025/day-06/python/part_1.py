def Part1(input):
    # Step 1: Parse input into grid
    # ---------------------------------------------
    grid: list[list[int]] = []
    lines = input.strip().splitlines()
    for line in lines:
        grid.append([int(x) if x.isdigit() else x for x in line.strip().split()])

    # Step 2: Transpose grid to something easy
    # ----------------------------------------------
    #
    # Initial grid:
    # ---------------------
    # 123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +
    #
    # Transpose grid to:
    # ---------------------
    # * 6 45 123
    # + 98 64 328
    # * 215 387 51
    # + 314 23 64
    grid = [list(col)[::-1] for col in zip(*grid)]

    # Step 3: Evaluate each row and sum results
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
