def my_pow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    for _ in range(n):
        result *= x
    return result
