# https://stackoverflow.com/questions/198199/how-do-you-reverse-a-string-in-place-in-c-or-c
# basically just swap from outside to center
def reverse_string(s):
    for i in range(len(s) // 2):
        j = len(s) - 1 - i
        temp = s[j]
        s[j] = s[i]
        s[i] = temp

    return s


assert reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
assert reverse_string(["H", "a", "n"]) == ["n", "a", "H"]


def reverse_string_v2(s):
    return " ".join([word[::-1] for word in s.split(' ')])


assert reverse_string_v2(
    "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverse_string_v2("God Ding") == "doG gniD"
