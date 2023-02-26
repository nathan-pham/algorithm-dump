from typing import List

# closer to combinations.py


def letter_permutations(s: str) -> List[str]:
    result = []

    def backtrack(start: int, comb: List[str]):
        # base case
        if len(comb) == len(s):
            result.append("".join(comb))
            return

        # decision tree
        for i in range(start, len(s)):
            if s[i].isalpha():
                comb.append(s[i].upper())
                backtrack(i + 1, comb)
                comb.pop()

                comb.append(s[i].lower())
                backtrack(i + 1, comb)
                comb.pop()
            else:
                comb.append(s[i])
                backtrack(i + 1, comb)
                comb.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(letter_permutations("a1b2"))
