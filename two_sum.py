def solution(array, target):
    if len(array) < 2:
        return None

    tabs = {}
    for i in range(len(array)):
        remainder = target - array[i]
        if remainder in tabs:
            return [tabs[remainder], i]

        tabs[array[i]] = i

    return None


assert solution([1, 3, 7, 9, 2], 11) == [3, 4]
assert solution([1, 6], 7) == [0, 1]

assert solution([1, 3, 7, 9, 2], 25) == None
assert solution([10], 10) == None
assert solution([], 10) == None
