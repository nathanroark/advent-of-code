import time

input = open("../data/input.txt", "r", encoding="utf-8").read()
test_input_1 = open("../data/test-input-1.txt", "r", encoding="utf-8").read()


def Part1Runner():
    from part_1 import Part1

    part_1_test_answer = 3
    part_1_final_answer = 674
    print("-------- Part 1 --------")
    test = Part1(test_input_1)
    if test != part_1_test_answer:
        print(f"❌ Test Result:  {test}, expected {part_1_test_answer}")
        return
    print(f"✅ Test Result:  {test}")

    start = time.time()
    final = Part1(input)
    stop = time.time()
    total_time = (stop - start) * 1000
    if final != part_1_final_answer:
        print(f"❌ Final Result: {final}, expected {part_1_final_answer}")
        return
    print(f"✅ Final Result: {final}")
    print(f"⏱️  Execution Time: {total_time:.2f} ms")


def Part2Runner():
    from part_2 import Part2

    part_2_test_answer = 3
    part_2_final_answer = 366
    print("-------- Part 2 --------")
    test = Part2(test_input_1)
    if test != part_2_test_answer:
        print(f"❌ Test Result:  {test}, expected {part_2_test_answer}")
        return
    print(f"✅ Test Result:  {test}")

    start = time.time()
    final = Part2(input)
    stop = time.time()
    total_time = (stop - start) * 1000
    if final != part_2_final_answer:
        print(f"❌ Final Result: {final}, expected {part_2_final_answer}")
        return
    print(f"✅ Final Result: {final}")
    print(f"⏱️  Execution Time: {total_time:.2f} ms")


if __name__ == "__main__":
    print("============ Day 05 ============")
    Part1Runner()
