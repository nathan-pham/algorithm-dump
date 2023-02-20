def squares_sorted_array(array):
    squares = list(sorted([item ** 2 for item in array]))
    return squares


assert squares_sorted_array([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert squares_sorted_array([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
