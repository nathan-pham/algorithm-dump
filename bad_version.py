def firstBadVersion(n, first_bad_version):
    def isBadVersion(x):
        return x >= first_bad_version

    pl, pr = 1, n
    ans = -1
    while pl <= pr:
        guess = (pl + pr) // 2
        if isBadVersion(guess):
            ans = guess
            pr = guess - 1
        else:
            pl = guess + 1

    return ans


assert firstBadVersion(5, 4) == 4
assert firstBadVersion(1, 1) == 1
