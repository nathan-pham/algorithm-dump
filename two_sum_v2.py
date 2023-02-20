# nums is sorted
# return indexes of pairs that equal target

def two_sum_v2(nums, target):
    pl, pr = 0, len(nums) - 1

    while pl < pr:
        win = nums[pl] + nums[pr]
        if win == target:
            return [pl + 1, pr + 1]

        if win < target:
            pl += 1
        else:
            pr -= 1


assert two_sum_v2([2, 7, 11, 15], 9) == [1, 2]
assert two_sum_v2([2, 3, 4], 6) == [1, 3]
assert two_sum_v2([-1, 0], -1) == [1, 2]
