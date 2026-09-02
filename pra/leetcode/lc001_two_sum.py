def two_sum(nums: list[int], target: int) -> list[int]:
    res = []
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", two_sum([2, 7, 11, 15], 9), [0, 1])
    check("middle pair", two_sum([3, 2, 4], 6), [1, 2])
    check("same value twice", two_sum([3, 3], 6), [0, 1])
