def max_area(height: list[int]) -> int:
    # TODO: implement with two pointers
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check("two elements", max_area([1, 1]), 1)
