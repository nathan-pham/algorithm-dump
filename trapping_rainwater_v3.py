def solution(el_map):
    if len(el_map) <= 2:
        return 0

    pl, pr = 0, len(el_map) - 1
    max_left, max_right = el_map[pl], el_map[pr]
    rainwater = 0
    while pl < pr:
        if max_left < max_right:
            pl += 1
            max_left = max(el_map[pl], max_left)
            rainwater += max_left - el_map[pl]
            # same formula
            # container height - current height
        else:
            pr -= 1
            max_right = max(el_map[pr], max_right)
            rainwater += max_right - el_map[pr]

    return rainwater


assert solution([9, 8, 2, 6]) == 4

assert solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
assert solution([4, 2, 0, 3, 2, 5]) == 9
assert solution([1, 0, 1]) == 1
assert solution([]) == 0
assert solution([1, 2]) == 0
assert solution([1, 2, 3]) == 0
