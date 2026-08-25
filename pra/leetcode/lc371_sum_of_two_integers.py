def get_sum(a: int, b: int) -> int:
    # TODO: implement (XOR for sum-without-carry, AND+shift for carry, repeat until no carry)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", get_sum(1, 2), 3)
    check("another pair", get_sum(2, 3), 5)
