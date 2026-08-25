def merge(intervals: list[list[int]]) -> list[list[int]]:
    # TODO: implement (sort by start without sorted(), then sweep and merge)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
    check("touching intervals", merge([[1, 4], [4, 5]]), [[1, 5]])
