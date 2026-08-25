def is_valid_parentheses(s: str) -> bool:
    # TODO: implement using a stack
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple pair", is_valid_parentheses("()"), True)
    check("multiple types", is_valid_parentheses("()[]{}"), True)
    check("mismatched types", is_valid_parentheses("(]"), False)
    check("wrong order", is_valid_parentheses("([)]"), False)
    check("nested", is_valid_parentheses("{[]}"), True)
