with open("./input.txt") as file:
    data = int(file.read().strip())
    lines = [
        "Start song",
        "Restart song",
        "Tempo up",
        "Tempo down",
        "Pause someone tripped",
        "Drop the bass",
        "Drop it lower!",
        "Pitch higher",
        "Pitch too high, shattering glass!",
        "Get my agent on the phone"
    ]

    print(lines[data])
