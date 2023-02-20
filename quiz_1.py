from english_words import long_word_list

print(len(long_word_list))

# Make a new list called alpha_words that contains only the words
# that are alphabetical, and display the length of the list.


def get_alpha_words():
    alpha_words = []
    for word in long_word_list:
        if sorted(word) == list(word):
            alpha_words.append(word)

    return alpha_words


alpha_words = get_alpha_words()
print(len(alpha_words))


# Find and display the longest word in alpha_words.

def get_longest_alpha_word(alpha_words):
    longest_word = None
    longest_length = 0
    for word in alpha_words:
        if len(word) > longest_length:
            longest_length = len(word)
            long_word = word

    return long_word


print(get_longest_alpha_word(alpha_words))

# Write a function called encompasses that takes two words
# returns True if the first word contains the second word
# but not at the beginning or the end (and False otherwise).
# For example, hippopotomus encompasses the word pot.


def encompasses(word_a, word_b):
    idx = word_a.find(word_b)
    return idx > 0 and idx + len(word_b) != len(word_a)


print(encompasses("hippopotamus", "popo"))

# Two words make a "reverse pair"
# if one of them is the reverse of the other.
# For example, pots and stop are a reverse pair.
# Make a list of all reverse pairs in word_list.
# Each pair of words should appear only once


def find_reverse_pairs():
    reverse_pairs = {}
    for word in long_word_list:
        word_reversed = "".join(list(reversed(word)))
        use_key = word if word in reverse_pairs else word_reversed
        reverse_pairs.setdefault(use_key, [])
        reverse_pairs[use_key].append(word)

    return [pair for pair in reverse_pairs.values() if len(pair) >= 2]


print(find_reverse_pairs())
