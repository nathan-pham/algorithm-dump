

def search_insert(array, target):
    # return index if found
    # otherwise return index where it should be inserted
    pl, pr = 0, len(array) - 1
    mid = 0
    while pl <= pr:
        mid = (pl + pr) // 2
        if array[mid] > target:
            pr = mid - 1
        elif array[mid] < target:
            pl = mid + 1
        else:
            return mid

    return pl


assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 7) == 4
assert search_insert([1, 3], 0) == 0
assert search_insert([1, 3], 2) == 1
assert search_insert([1, 3], 4) == 2
assert search_insert([1, 3, 5], 4) == 2
