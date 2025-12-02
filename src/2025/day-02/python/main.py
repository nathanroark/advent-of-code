input = open("../data/input.txt", "r", encoding="utf-8").read()
test_input_1 = open("../data/test-input-1.txt", "r", encoding="utf-8").read()


def Part1Runner():
    from part_1 import Part1

    part_1_test_answer = 1227775554
    part_1_final_answer = 19574776074
    print("-------- Part 1 --------")
    test = Part1(test_input_1)
    if test == part_1_test_answer:
        print(f"✅ Test Result:  {test}")
    else:
        print(f"❌ Test Result:  {test}, expected {part_1_test_answer}")
        return
    final = Part1(input)
    if final == part_1_final_answer:
        print(f"✅ Final Result: {final}")
    else:
        print(f"❌ Final Result: {final}, expected {part_1_final_answer}")
        return


def Part2Runner():
    from part_2 import Part2

    part_2_test_answer = 4174379265
    part_2_final_answer = 25912654282
    print("-------- Part 2 --------")
    test = Part2(test_input_1)
    if test == part_2_test_answer:
        print(f"✅ Test Result:  {test}")
    else:
        print(f"❌ Test Result:  {test}, expected {part_2_test_answer}")
        return
    final = Part2(input)
    if final == part_2_final_answer:
        print(f"✅ Final Result: {final}")
    else:
        print(f"❌ Final Result: {final}, expected {part_2_final_answer}")
        return


if __name__ == "__main__":
    print("============ Day 02 ============")
    Part1Runner()
    Part2Runner()
