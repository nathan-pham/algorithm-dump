def rotate_array(array, k):
    array_copy = [*array]
    for i in range(len(array)):
        array[(i + k) % len(array)] = array_copy[i]

    return array


assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


def rotate_array_v2(array, k):
    n = (len(array) - k) % len(array)
    array[:] = array[n:] + array[:n]
    return array


assert rotate_array_v2([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate_array_v2([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
