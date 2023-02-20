def search(array, target):
    pl, pr = 0, len(array) - 1
    while pl <= pr:
        mid = (pr + pl) // 2
        if array[mid] > target:
            pr = mid - 1
        elif array[mid] < target:
            pl = mid + 1
        else:
            return mid

    return - 1


assert search([-1, 0, 3, 5, 9, 12], 9) == 4
assert search([-1, 0, 3, 5, 9, 12], 2) == -1
assert search([5], 5) == 0
assert search([], 10) == -1
