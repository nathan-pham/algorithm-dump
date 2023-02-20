def pivot_index(array):
    total_sum = sum(array)
    lhs = 0
    for i in range(len(array)):
        rhs = total_sum - lhs - array[i]
        if lhs == rhs:
            return i

        lhs += array[i]

    return -1


assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
assert pivot_index([1, 2, 3]) == -1
assert pivot_index([2, 1, -1]) == 0
assert pivot_index([]) == -1
