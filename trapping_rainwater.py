def solution(el_map):
    if len(el_map) <= 2:
        return 0

    # this solution basically finds the amount of water
    # above any given point & adds up the results
    rainwater = 0
    for i in range(len(el_map)):
        # get max bound to the left
        max_h_left = 0
        for h in el_map[:i]:
            if h > max_h_left:
                max_h_left = h

        # get max bound to the right
        max_h_right = 0
        j = i + 1
        for h in el_map[j:]:
            if h > max_h_right:
                max_h_right = h

                # the water above a particular cell
                # min bound - current height
        water_above = min(max_h_left, max_h_right) - el_map[i]
        if water_above > 0:
            rainwater += water_above

    return rainwater


assert solution([9, 8, 2, 6]) == 4

assert solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
assert solution([4, 2, 0, 3, 2, 5]) == 9
assert solution([1, 0, 1]) == 1

assert solution([]) == 0
assert solution([1, 2]) == 0
assert solution([1, 2, 3]) == 0
