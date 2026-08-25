def inter(s1: str, s2: str) -> str:
    # TODO: set()を使わずに実装する
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", inter("hello", "world"), "lo")
    check("with duplicates in s1", inter("banana", "band"), "ban")
    check("s2 shorter", inter("abcabc", "bc"), "bc")
    check("no overlap", inter("abc", "xyz"), "")
    check("empty s1", inter("", "abc"), "")
