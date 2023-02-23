from typing import Optional, List


def nearest_one(matrix: List[List[int]]) -> List[List[int]]:
    height, width = len(matrix), len(matrix[0])
    queue = []

    # loop through every cell
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                queue.append((i, j))
            else:
                matrix[i][j] = "#"

    for (i, j) in queue:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + dx
            nj = j + dy

            if 0 <= ni < height and 0 <= nj < width and matrix[ni][nj] == '#':
                matrix[ni][nj] = matrix[i][j] + 1
                queue.append((ni, nj))

    print(matrix)
    return matrix


def equals(matrix_a: Optional[List[List[int]]], matrix_b: Optional[List[List[int]]]):
    if matrix_a is None or matrix_b is None:
        return False

    size_a = (len(matrix_a), len(matrix_a[0]))
    size_b = (len(matrix_b), len(matrix_b[0]))

    if size_a != size_b:
        return False

    h, w = size_a
    for i in range(h):
        for j in range(w):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False

    return True


if __name__ == "__main__":
    assert equals(
        nearest_one([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    )

    assert equals(
        nearest_one([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    )
