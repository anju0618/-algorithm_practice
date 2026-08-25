def find_target_sum_ways(nums: list[int], target: int) -> int:
    # TODO: implement (DP over achievable running sums, shifted to a non-negative index)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_target_sum_ways([1, 1, 1, 1, 1], 3), 5)
    check("single element", find_target_sum_ways([1], 1), 1)
