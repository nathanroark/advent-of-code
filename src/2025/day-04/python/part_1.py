def Part1(input):
    neighbors = (
        (-1, -1),  # Above left
        (-1, 0),  # Above
        (-1, 1),  # Above right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Below left
        (1, 0),  # Below
        (1, 1),  # Below right
    )
    alive_cells = set()
    num_neighbors = dict()
    board = []

    lines = input.strip().splitlines()
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        board.append(lines[i])
        for j in range(m):
            if lines[i][j] == "@":
                alive_cells.add((i, j))
            num_neighbors[(i, j)] = 0

    for row, col in alive_cells:
        for drow, dcol in neighbors:
            # if out of bounds, wrap around
            # if 0 > row + drow:
            #     wrapped_row = n - 1
            # elif row + drow >= n:
            #     wrapped_row = 0
            # else:
            #     wrapped_row = row + drow
            #
            # if 0 > col + dcol:
            #     wrapped_col = m - 1
            # elif col + dcol >= m:
            #     wrapped_col = 0
            # else:
            #     wrapped_col = col + dcol
            # num_neighbors[(row + drow, col + dcol)] += 1
            # if not '.'
            new_row = row + drow
            new_col = col + dcol
            # skip if out of bounds
            if 0 > new_row or new_row >= n or 0 > new_col or new_col >= m:
                continue
            if board[new_row][new_col] == "@":
                num_neighbors[(new_row, new_col)] += 1

    print_board = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    # turn print_board into a list of lists
    print_board = [list(row) for row in print_board]

    # number of cells with less than 4 neighbors
    count = 0
    for cell, neighbors in num_neighbors.items():
        # print_board[cell[0]][cell[1]] = str(neighbors)
        if neighbors < 4 and board[cell[0]][cell[1]] == "@":
            count += 1
            # set print_board cell to X
            # print_board[cell[0]][cell[1]] = "x"

    # print("Final Board:")
    # for row in print_board:
    #     print("".join(row))
    return count
