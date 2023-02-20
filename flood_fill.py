from typing import List


def print_grid(grid: List[List[int]]):
    for row in grid:
        print(', '.join([str(item) for item in row]))


def flood_fill(grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    target_value = grid[sr][sc]
    if color == target_value:
        return grid

    stack = [(sr, sc)]
    h, w = len(grid), len(grid[0])

    while len(stack) > 0:
        i, j = stack.pop()
        if grid[i][j] == target_value:
            grid[i][j] = color
            if i - 1 >= 0:
                stack.append((i - 1, j))
            if i + 1 < h:
                stack.append((i + 1, j))
            if j - 1 >= 0:
                stack.append((i, j - 1))
            if j + 1 < w:
                stack.append((i, j + 1))

    return grid


if __name__ == "__main__":
    assert str(flood_fill(
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        1, 1, 2
    )) == str([[2, 2, 2], [2, 2, 0], [2, 0, 1]])

    assert str(flood_fill(
        [[0, 0, 0], [0, 0, 0]],
        0, 0, 0
    )) == str([[0, 0, 0], [0, 0, 0]])
