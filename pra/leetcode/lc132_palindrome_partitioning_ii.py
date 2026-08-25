def min_palindrome_cuts(s: str) -> int:
    # TODO: implement (DP)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("one cut needed", min_palindrome_cuts("aab"), 1)
    check("single char", min_palindrome_cuts("a"), 0)
    check("two distinct chars", min_palindrome_cuts("ab"), 1)
