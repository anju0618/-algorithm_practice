def max_sub_array(nums: list[int]) -> int:
    # TODO: implement (Kadane's algorithm)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    check("all positive", max_sub_array([5, 4, -1, 7, 8]), 23)
