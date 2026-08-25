def single_number(nums: list[int]) -> int:
    # TODO: implement (XOR everything together)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", single_number([2, 2, 1]), 1)
    check("longer array", single_number([4, 1, 2, 1, 2]), 4)
