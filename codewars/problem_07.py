import os
from os.path import abspath


dir_location_unresolved = ""
dir_location = ""
drone = ""
with open("./input.txt") as file:
    data = [line.strip() for line in file.read().strip().split('\n')]
    dir_location_unresolved = data[0]
    dir_location = abspath(f"./{data[0]}")
    drone = data[1]

text_files = [f"{dir_location}/{file}" for file in os.listdir(
    dir_location) if file.endswith(".txt")]

for path in text_files:
    with open(path) as file:
        if drone in file.read():
            print(f"{drone} was found Under {dir_location_unresolved}")
