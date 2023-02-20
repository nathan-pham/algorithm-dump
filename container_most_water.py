def get_max_area(array):
    pl, pr = 0, len(array) - 1
    max_area = 0
    while pl <= pr:
        area = min(array[pl], array[pr]) * (pr - pl)
        max_area = max(max_area, area)

        if array[pl] < array[pr]:
            pl += 1
        else:
            pr -= 1

    return max_area


assert get_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert get_max_area([2, 3, 4, 5, 18, 17, 6]) == 17
assert get_max_area([1, 1]) == 1
