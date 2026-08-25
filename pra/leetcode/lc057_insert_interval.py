def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # TODO: implement (three phases: before overlap, merge overlap, after overlap)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
    check("merges several", insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])
