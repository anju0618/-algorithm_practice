def is_happy(n: int) -> bool:
    # TODO: implement (repeat sum-of-squared-digits; detect a cycle with a dict)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("happy", is_happy(19), True)
    check("not happy", is_happy(2), False)
