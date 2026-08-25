def count_substrings(s: str) -> int:
    # TODO: implement (expand around each center, count every valid expansion)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("no repeats", count_substrings("abc"), 3)
    check("all same char", count_substrings("aaa"), 6)
