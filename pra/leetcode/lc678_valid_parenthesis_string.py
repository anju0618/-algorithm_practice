def check_valid_string(s: str) -> bool:
    # TODO: implement (track the range [low, high] of possible open-paren counts)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple pair", check_valid_string("()"), True)
    check("star as nothing", check_valid_string("(*)"), True)
    check("star as open", check_valid_string("(*))"), True)
