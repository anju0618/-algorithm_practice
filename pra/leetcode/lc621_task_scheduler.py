def least_interval(tasks: list[str], n: int) -> int:
    # TODO: implement (frequency-based formula, no heap needed here)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("needs idle slots", least_interval(["A", "A", "A", "B", "B", "B"], 2), 8)
    check("no idle needed", least_interval(["A", "C", "A", "B", "D", "B"], 1), 6)
