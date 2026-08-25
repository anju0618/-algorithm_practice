def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # TODO: implement (sort starts and ends separately without sorted(), two-pointer sweep)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("needs two rooms", min_meeting_rooms([[0, 30], [5, 10], [15, 20]]), 2)
    check("needs one room", min_meeting_rooms([[7, 10], [2, 4]]), 1)
