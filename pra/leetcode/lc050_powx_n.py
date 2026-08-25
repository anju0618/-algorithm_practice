def my_pow(x: float, n: int) -> float:
    # TODO: implement (binary exponentiation, handle negative n)
    pass


def check(label, actual, expected):
    ok = abs(actual - expected) < 1e-5
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", my_pow(2.0, 10), 1024.0)
    check("non-integer base", my_pow(2.1, 3), 9.261)
    check("negative exponent", my_pow(2.0, -2), 0.25)
