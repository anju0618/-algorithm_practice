def search(nums: list[int], target: int) -> int:
    # TODO: implement classic binary search
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("found", search([-1, 0, 3, 5, 9, 12], 9), 4)
    check("not found", search([-1, 0, 3, 5, 9, 12], 2), -1)
