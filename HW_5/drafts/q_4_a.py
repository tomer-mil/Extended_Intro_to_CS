def power_new(a, b):
    result = 1

    b_bin = bin(b)[2:]

    reverse_b_bin = b_bin[::-1]

    for bit in reverse_b_bin:
        if bit == "1":
            result = result * a
        a = a * a

    return result


def power_with_base(a, b, base=2):

    assert base >= 2
    result = 1

    while b > 0:

        x = 1

        residual = b % base

        for i in range(residual):
            x *= a

        result *= x

        for i in range(base - residual):
            x *= a

        a = x
        b = b // base

    return result


print(power_with_base(2, 7, 3))