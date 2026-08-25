def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    # TODO: implement (sort intervals by start and queries by value, sweep with a hand-rolled min-heap keyed by interval size)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]), [3, 3, 1, 4])
    check("some unmatched", min_interval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), [2, -1, 4, 6])
