def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    freq = {}
    for char in word1:
        freq[char] = freq.get(char, 0) + 1

    for char in word2:
        if freq.get(char, 0) <= 0:
            return False

        freq[char] = freq.get(char) - 1

    return True        

if __name__ == "__main__":
    print(is_anagram("tachymetric", "mccarthyite")) # True