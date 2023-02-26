from typing import List


def permutations(nums: List[int]):
    results = []

    # base case
    # create copy of nums
    if len(nums) == 1:
        return [nums[:]]

    for _ in range(len(nums)):
        # get all permutations without n
        n = nums.pop(0)
        perms = permutations(nums)

        # stick n back in
        for perm in perms:
            perm.append(n)

        results.extend(perms)
        nums.append(n)

    return results


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
