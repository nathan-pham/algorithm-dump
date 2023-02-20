from typing import List


# uses DFS (ie: stack)
# naive approach
# similar to flood_fill.py
def max_area_island(grid: List[List[int]]):
    # get potential starting points of each island
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                nodes.append((i, j))

    # compute areas of each starting point
    areas = []
    for node in nodes:
        stack = [node]
        area = 0
        while len(stack) > 0:
            i, j = stack.pop()
            if grid[i][j] == 1:
                grid[i][j] = -1  # we've visited this before
                area += 1
                if i + 1 < len(grid):
                    stack.append((i + 1, j))
                if i - 1 >= 0:
                    stack.append((i - 1, j))
                if j + 1 < len(grid[0]):
                    stack.append((i, j + 1))
                if j - 1 >= 0:
                    stack.append((i, j - 1))

        areas.append(area)

    # find the max area
    return max(areas or [0])


if __name__ == "__main__":
    assert max_area_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6

    assert max_area_island([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
