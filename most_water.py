def solution(array):
    if len(array) < 2:
        return 0

    max_area = 0

    pl = 0
    pr = len(array) - 1
    while pl < pr:
        width, height = pr - pl, min(array[pl], array[pr])
        area = width * height
        if area > max_area:
            max_area = area

        # we move which ever pointer is smaller first
        # smaller = impacts calculation in min(array[pl], array[pr])
        if array[pl] < array[pr]:
            pl += 1
        else:
            pr -= 1

    return max_area


assert solution([4, 8, 1, 2, 3, 9]) == 32
assert solution([7, 1, 2, 3, 9]) == 28  # 7 * 4 = 28
assert solution([1]) == 0  # 0
assert solution([]) == 0  # 0

assert solution([1, 8, 6, 2, 9, 4]) == 24
