def missing_number(nums: list[int]) -> int:
    # TODO: implement (compare expected sum 0..n against the actual sum)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("missing middle", missing_number([3, 0, 1]), 2)
    check("missing last", missing_number([0, 1]), 2)
    check("larger array", missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
