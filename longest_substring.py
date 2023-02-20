def longest_substring(s):
    win_start = 0
    win_end = 0
    win_len = 0
    seen = set()

    while win_end < len(s):
        char = s[win_end]

        if char not in seen:
            win_end += 1
            win_len = max(win_len, win_end - win_start)
            seen.add(char)
        else:
            seen.remove(s[win_start])
            win_start += 1

    return win_len


if __name__ == "__main__":
    assert longest_substring("abcabcbb") == 3
    assert longest_substring("bbbbb") == 1
    assert longest_substring("pwwkew") == 3
    assert longest_substring("a") == 1
    assert longest_substring("au") == 2
    assert longest_substring("aab") == 2
    assert longest_substring("aabaab!bb") == 3
