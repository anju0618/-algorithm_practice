def string_permutation_checker(s1: str, s2: str) -> bool:
    # TODO: implement without sorted()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic permutation", string_permutation_checker("abc", "bca"), True)
    check("not a permutation", string_permutation_checker("abc", "def"), False)
    check("longer permutation", string_permutation_checker("listen", "silent"), True)
    check("one char different", string_permutation_checker("hello", "bello"), False)
    check("both empty", string_permutation_checker("", ""), True)
    check("length mismatch", string_permutation_checker("a", ""), False)
    check("case sensitive", string_permutation_checker("Abc", "abc"), False)
    check("with spaces", string_permutation_checker("a gentleman", "elegant man"), True)
