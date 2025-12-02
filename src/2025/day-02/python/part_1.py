def Part1(input):
    data = input.strip().split(",")
    for d in data:
        id = d.split("-")
        first_id, last_id = id[0], id[1]
        print("--------------")
        print(f"{first_id}")
        print(f"{last_id}")
        print("--------------")
