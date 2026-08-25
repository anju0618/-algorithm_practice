def can_attend_meetings(intervals: list[list[int]]) -> bool:
    # TODO: implement (sort by start without sorted(), check for any overlap)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("overlapping", can_attend_meetings([[0, 30], [5, 10], [15, 20]]), False)
    check("no overlap", can_attend_meetings([[7, 10], [2, 4]]), True)
