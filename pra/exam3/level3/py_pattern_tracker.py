def pattern_tracker(text: str) -> int:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple ascending", pattern_tracker("123"), 2)
    check("with letters", pattern_tracker("12a34"), 2)
    check("descending, no matches", pattern_tracker("987654321"), 0)
    check("full ascending run", pattern_tracker("01234567"), 7)
    check("no digits", pattern_tracker("abc"), 0)
    check("digits separated by letters", pattern_tracker("1a2b3c4"), 0)
    check("two separate pairs", pattern_tracker("112233"), 2)
