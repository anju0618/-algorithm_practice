def string_sculptor(text: str) -> str:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", string_sculptor("hello"), "hElLo")
    check("space resets alternation", string_sculptor("Hello World"), "hElLo wOrLd")
    check("digits skipped from index", string_sculptor("abc123def"), "aBc123DeF")
    check("mixed punctuation", string_sculptor("Python3.9!"), "pYtHoN3.9!")
    check("empty string", string_sculptor(""), "")
