def anagram(s1: str, s2: str) -> bool:
    # TODO: implement without sorted()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", anagram("listen", "silent"), True)
    check("case insensitive", anagram("Triangle", "Integral"), True)
    check("with spaces", anagram("Dormitory", "Dirty Room"), True)
    check("not anagram", anagram("hello", "world"), False)
    check("both empty", anagram("", ""), True)
    check("different length", anagram("abc", "abcc"), False)
