def Part2(input):
    lines = input.splitlines()
    rows = len(lines)
    cols = len(lines[0])

    result_sum = 0
    current_operation = None
    current_result = None

    # Step 1: Process each column from left to right
    # -----------------------------------------------------
    for c in range(cols):
        # Step 1a: Read column top to bottom, combine digits
        # -------------------------------------------------
        current_number = ""
        for r in range(rows):
            char = lines[r][c]
            if char.isdigit():
                current_number += char
            elif char in ["*", "+"]:
                # Save previous calculation when we hit a new operator
                if current_result is not None:
                    result_sum += current_result
                    current_result = None
                current_operation = char

        # Step 1b: Process the number we collected
        # ---------------------------------------------
        if current_number:
            num = int(current_number)
            if current_result is None:
                current_result = num
            else:
                if current_operation == "*":
                    current_result *= num
                elif current_operation == "+":
                    current_result += num

    # Add the last result to the sum
    # (just because we didn't have an operator after it to trigger the addition)
    if current_result is not None:
        result_sum += current_result

    return result_sum
