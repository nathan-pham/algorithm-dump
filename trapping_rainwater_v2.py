def solution(el_map):
    if len(el_map) <= 2:
        return 0

    left_maxes = [0] * len(el_map)
    right_maxes = [0] * len(el_map)
    min_maxes = [0] * len(el_map)
    left_max = 0
    right_max = 0
    for i in range(len(el_map)):
        left_maxes[i] = left_max
        el = el_map[i]
        if el > left_max:
            left_max = el

        j = len(el_map) - i - 1
        right_maxes[j] = right_max
        el = el_map[j]
        if el > right_max:
            right_max = el

    for i in range(len(el_map)):
        min_maxes[i] = min(left_maxes[i], right_maxes[i])

    rainwater = 0
    for i in range(len(el_map)):
        rainwater += max(0, min_maxes[i] - el_map[i])

    return rainwater


assert solution([9, 8, 2, 6]) == 4

assert solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
assert solution([4, 2, 0, 3, 2, 5]) == 9
assert solution([1, 0, 1]) == 1
assert solution([]) == 0
assert solution([1, 2]) == 0
assert solution([1, 2, 3]) == 0
