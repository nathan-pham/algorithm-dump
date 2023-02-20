def S(n):
    result = 0
    for i in range(n + 1):
        result += i

    return result


assert S(1) == 1
assert S(3) == 6
assert S(4) == 10
