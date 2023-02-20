import timeit

from english_words import long_word_list
from is_anagram import is_anagram

print(f"length of long_word_list = {len(long_word_list)}")

def all_anagram_pairs(word_list):
    pairs = {}
    for word in word_list:
        sorted_word = "".join(sorted(list(word)))
        pairs[sorted_word] = pairs.get(sorted_word, []) + [word]

    max_length = 0
    max_pair = []
    for pair in pairs.values():
        if len(pair) > max_length:
            max_length = len(pair)
            max_pair = pair

    return max_pair
    # return [value for value in pairs.values() if len(value) >= 2]


number = 1
duration = timeit.Timer(lambda : all_anagram_pairs(long_word_list)).timeit(number = number)
print(f"run time = {(duration / number):.10f}s with {number} trials")

print((all_anagram_pairs(long_word_list)))