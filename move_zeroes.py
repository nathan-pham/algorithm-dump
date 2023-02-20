def move_zeroes(nums):
    i_nonzero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i_nonzero] = nums[i]
            i_nonzero += 1

    for i in range(i_nonzero, len(nums)):
        nums[i] = 0

    return nums


assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeroes([1, 0, 1]) == [1, 1, 0]
assert move_zeroes([0]) == [0]
