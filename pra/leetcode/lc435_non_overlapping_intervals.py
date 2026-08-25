def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # TODO: implement (sort by end time without sorted(), greedily keep earliest-ending intervals)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
    check("all identical", erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)
