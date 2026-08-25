def is_valid_palindrome(s: str) -> bool:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("classic example", is_valid_palindrome("A man, a plan, a canal: Panama"), True)
    check("not a palindrome", is_valid_palindrome("race a car"), False)
    check("empty string", is_valid_palindrome(""), True)
