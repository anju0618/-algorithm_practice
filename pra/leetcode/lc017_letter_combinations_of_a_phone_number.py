def letter_combinations(digits: str) -> list[str]:
    # TODO: implement (backtracking over the keypad mapping)
    pass


def check(label, actual, expected):
    ok = sorted(actual) == sorted(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("two digits", letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    check("one digit", letter_combinations("2"), ["a", "b", "c"])
    check("empty input", letter_combinations(""), [])
