def t(num):
    return float(f"{(num - 0.05):.1f}")


with open("./input.txt") as file:
    data = [[float(word) for word in line.strip().split(' ')]
            for line in file.read().strip().split('\n')[:-1]]

    total = 0
    for line in data:
        diff = t(line[1] - line[0])
        total += diff
        print(f"DIFF: {diff}")

    print(f"TOTAL: {total}")
