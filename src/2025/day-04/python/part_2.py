def Part2(input):
    neighbors_offsets = (
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
    lines = input.strip().splitlines()
    n = len(lines)
    m = len(lines[0])

    # Parse initial alive cells
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "@":
                alive_cells.add((i, j))

    total_count = 0

    while True:
        # Count neighbors for each cell
        num_neighbors = dict()
        for row, col in alive_cells:
            for drow, dcol in neighbors_offsets:
                new_row = row + drow
                new_col = col + dcol
                # Skip if out of bounds
                if 0 > new_row or new_row >= n or 0 > new_col or new_col >= m:
                    continue
                if (new_row, new_col) in alive_cells:
                    num_neighbors[(row, col)] = num_neighbors.get((row, col), 0) + 1

        # Find cells to remove (alive cells with < 4 neighbors)
        cells_to_remove = set()
        for cell in alive_cells:
            if num_neighbors.get(cell, 0) < 4:
                cells_to_remove.add(cell)

        # Remove cells
        count = len(cells_to_remove)
        if count == 0:
            break

        alive_cells -= cells_to_remove
        total_count += count

    return total_count
