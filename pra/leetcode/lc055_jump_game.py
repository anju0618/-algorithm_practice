def can_jump(nums: list[int]) -> bool:
    # TODO: implement (track the farthest reachable index greedily)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("reachable", can_jump([2, 3, 1, 1, 4]), True)
    check("stuck at a zero", can_jump([3, 2, 1, 0, 4]), False)
