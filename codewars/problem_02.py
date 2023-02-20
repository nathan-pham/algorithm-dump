with open("./input.txt") as file:
    data = [int(line.strip()) for line in file.read().strip().split('\n')]
    E, M = data[0], data[1]
    result = E * M
    print(result)
    if result > 500_000:
        print("Too Many Bugs! Abandon Game!!")
