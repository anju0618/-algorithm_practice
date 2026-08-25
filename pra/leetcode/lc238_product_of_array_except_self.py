def product_except_self(nums: list[int]) -> list[int]:
    # TODO: implement without division (prefix/suffix products)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    check("with zero", product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
