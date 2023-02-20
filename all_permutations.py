# back tracking

def all_permutations(array):
    result = []

    if len(array) == 1:
        return [array[:]]

    for _ in range(len(array)):
        n = array.pop(0)

        # find all permutations
        perms = all_permutations(array)
        for perm in perms:
            perm.append(n)

        # add them to results
        result.extend(perms)
        array.append(n)

    return result


if __name__ == "__main__":
    print(all_permutations([1, 2, 3]))
    print(all_permutations([1]))
