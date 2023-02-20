import os

short_word_list = ["proudest", "stop", "pots", "tops", "sprouted"]
long_word_list = []
with open("english_words.txt") as file:
    long_word_list = tuple(set([word.strip().lower() for word in file.read().split('\n')]))

if __name__ == "__main__":
    print(f"length of long_word_list = {len(long_word_list)}")
