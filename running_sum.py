def running_sum(array):
    sums = [0] * len(array)
    for i in range(len(array)):
        # technically not the most accurate
        # i - 1 will get the -1 idx in the array, which is fine because sums[-1] = 0 anyways
        sums[i] = sums[i - 1] + array[i]

    return sums


assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
