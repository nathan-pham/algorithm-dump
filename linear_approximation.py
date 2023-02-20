# linear approximation to estimate roots
# yes, we use ** in here which completely defeats the purpose of this
def linear_approximation(x, root):
    f = int((x ** root) + 0.5)  # get f(a)
    a = int(f ** (1 / root))  # reconstruct a from f
    f_prime = root * a ** ((root) - 1)  # get f'(a)

    # tangent line formula
    return f_prime * (x - a) + f


def close(float_a, float_b, tolerance=0.001):
    return abs(float_a - float_b) < tolerance


assert close(linear_approximation(79, 1 / 4), 161 / 54)
assert close(linear_approximation(17, 1 / 4), 65 / 32)
assert close(linear_approximation(15, 1 / 4), 63 / 32)
assert close(linear_approximation(29, 1 / 3), 83 / 27)
assert close(linear_approximation(9, 1 / 3), 25 / 12)
