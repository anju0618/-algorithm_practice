def daily_temperatures(temperatures: list[int]) -> list[int]:
    # TODO: implement with a monotonic stack
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
    check("strictly increasing", daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
    check("large jump", daily_temperatures([30, 60, 90]), [1, 1, 0])
