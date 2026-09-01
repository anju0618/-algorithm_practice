def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x != 0:
        digit = x % 10
        x //= 10
        result = result * 10 + digit

    result *= sign

    int_max = 2 ** 31 - 1
    int_min = -(2 ** 31)
    if result < int_min or result > int_max:
        return 0
    return result
