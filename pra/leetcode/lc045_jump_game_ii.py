def jump(nums: list[int]) -> int:
    # TODO: implement (BFS-like greedy: jump when you exhaust the current window)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", jump([2, 3, 1, 1, 4]), 2)
    check("with a zero", jump([2, 3, 0, 1, 4]), 2)
