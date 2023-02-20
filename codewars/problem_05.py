with open("./input.txt") as file:
    data = [line.strip() for line in file.read().strip().split('\n')][:-1]
    all_correct = True
    for line in data:
        ops, answer = [piece.strip() for piece in line.split('=')]
        real_answer = eval(ops)
        if str(real_answer) != str(answer):
            all_correct = False
            print(
                f"DIRECTIVE: {ops} != {answer}; CORRECT TO VALUE: {real_answer}")

    if all_correct:
        print("ALL DATASETS WERE CORRECT")
