def Part2(input):
    # Step 1: Parse input into grid
    # -----------------------------------------
    grid = []
    lines = input.splitlines()
    n = len(lines)
    m = len(lines[0])

    for c in range(m):
        if c >= len(grid):
            grid.append([])
        for r in range(n):
            char = lines[r][c]
            if char.isdigit():
                grid[c].append(int(char))
            else:
                grid[c].append(char)

    # Step 2: Combine digits into numbers
    # -----------------------------------------
    for r in range(len(grid)):
        new_row = []
        current_number = ""
        for item in grid[r]:
            if isinstance(item, int):
                current_number += str(item)
            else:
                if current_number:
                    new_row.append(int(current_number))
                    current_number = ""
                new_row.append(item)
        if current_number:
            new_row.append(int(current_number))
        grid[r] = new_row

    # Step 3: Clean up grid
    # -----------------------------------------
    # Step 3a: Remove spaces
    # -----------------------------------
    cleaned_grid = []
    for row in grid:
        cleaned_row = [item for item in row if item != " "]
        if cleaned_row:
            cleaned_grid.append(cleaned_row)

    # Step 3b: Move operators to front
    # -----------------------------------
    for i in range(len(cleaned_grid)):
        row = cleaned_grid[i]
        if row and isinstance(row[-1], str):
            operator = row.pop()
            row.insert(0, operator)

    # Step 4: Evaluate - Fixed logic
    # -----------------------------------------
    result_sum = 0
    current_operation = None
    current_result = None

    for row in cleaned_grid:
        for item in row:
            if isinstance(item, str):
                # New operator found - save previous result
                if current_result is not None:
                    result_sum += current_result
                    current_result = None
                current_operation = item
            else:
                # Process number
                if current_result is None:
                    current_result = item
                else:
                    if current_operation == "*":
                        current_result *= item
                    elif current_operation == "+":
                        current_result += item

    # Add final result
    if current_result is not None:
        result_sum += current_result

    return result_sum
