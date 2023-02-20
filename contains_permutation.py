def contains_permutation(s1, s2):
    if len(s1) > len(s2):
        return False

    freq_a, freq_b = ([0] * 26, [0] * 26)
    def get_i(char): return ord(char) - ord('a')

    for i in range(len(s1)):
        freq_a[get_i(s1[i])] += 1
        freq_b[get_i(s2[i])] += 1

    # compute existing matches
    matches = 0
    for i in range(26):
        if freq_a[i] == freq_b[i]:
            matches += 1

    # sliding window technique
    # freq_b is the window
    # matches just reduces time complexity from O(26 * n) -> O(n)
    l = 0
    for r in range(len(s1), len(s2)):
        # frequencies match, permutation found
        if matches == 26:
            return True

        # look at right pointer (we add to freq)
        i = get_i(s2[r])
        freq_b[i] += 1
        if freq_a[i] == freq_b[i]:  # match is now the same
            matches += 1
        elif freq_a[i] + 1 == freq_b[i]:  # we made freq_b too big
            matches -= 1

        # look at left pointer (we're shifting right so we sub from freq)
        i = get_i(s2[l])
        freq_b[i] -= 1
        if freq_a[i] == freq_b[i]:  # match is now the same
            matches += 1
        elif freq_a[i] - 1 == freq_b[i]:  # we made freq_b too small
            matches -= 1

        l += 1

    return matches == 26


if __name__ == "__main__":
    assert contains_permutation("ab", "eidbaooo") == True
    assert contains_permutation("ab", "eidboaoo") == False
    assert contains_permutation("a", "ab") == True
    assert contains_permutation("adc", "dcda") == True
