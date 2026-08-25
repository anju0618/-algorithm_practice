def longest_palindrome(s: str) -> str:
    # TODO: implement (expand around each center, odd and even length)
    pass


def check(label, actual, expected_options):
    status = "[OK]" if actual in expected_options else "[NG]"
    print(f"{status} {label}")
    if actual not in expected_options:
        print(f"      got:      {actual}")
        print(f"      expected one of: {expected_options}")


if __name__ == "__main__":
    check("multiple valid answers", longest_palindrome("babad"), ["bab", "aba"])
    check("even length", longest_palindrome("cbbd"), ["bb"])
