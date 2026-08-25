def can_partition(nums: list[int]) -> bool:
    # TODO: implement (0/1 knapsack: can we hit target = total // 2)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("can partition", can_partition([1, 5, 11, 5]), True)
    check("cannot partition", can_partition([1, 2, 3, 5]), False)
