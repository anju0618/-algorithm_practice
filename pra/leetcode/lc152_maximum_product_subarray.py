def max_product(nums: list[int]) -> int:
    # TODO: implement (track running max AND min, since a negative can flip them)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_product([2, 3, -2, 4]), 6)
    check("with zero", max_product([-2, 0, -1]), 0)
