from typing import List
from flood_fill import print_grid


# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange
def rotting_oranges(matrix: List[List[int]]) -> int:
    height, width = len(matrix), len(matrix[0])
    rot_steps = set()

    q = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                q.append((i, j, 0))

    for (i, j, lvl) in q:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + dx, j + dy
            if 0 <= ni < height and 0 <= nj < width and matrix[ni][nj] == 1:
                matrix[ni][nj] = 2
                q.append((ni, nj, lvl + 1))

        rot_steps.add(lvl)

    # check for oranges that didn't rot
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return -1

    # return steps
    return max(len(rot_steps) - 1, 0)


if __name__ == "__main__":
    assert rotting_oranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert rotting_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert rotting_oranges([[0]]) == 0
    assert rotting_oranges([[0, 2]]) == 0
