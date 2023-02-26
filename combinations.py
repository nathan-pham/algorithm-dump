from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, comb: List[int]):
        # tree has a max height of k
        if len(comb) == k:
            result.append(comb[:])
            return

        # decision tree
        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()

    backtrack(1, [])

    return result


if __name__ == "__main__":
    assert str(combine(4, 2)) == str(
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

    assert str(combine(1, 1)) == str([[1]])
