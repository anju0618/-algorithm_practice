def plus_one(digits: list[int]) -> list[int]:
    # TODO: implement (add 1 from the last digit, propagate any carry)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("no carry", plus_one([1, 2, 3]), [1, 2, 4])
    check("single carry", plus_one([4, 3, 2, 1]), [4, 3, 2, 2])
    check("full carry", plus_one([9, 9]), [1, 0, 0])
