def bracket_validator(s: str) -> bool:
    # TODO: implement using a stack
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple pair", bracket_validator("()"), True)
    check("multiple types", bracket_validator("()[]{}"), True)
    check("mismatched types", bracket_validator("(]"), False)
    check("wrong order", bracket_validator("([)]"), False)
    check("nested", bracket_validator("{[]}"), True)
    check("with other chars", bracket_validator("hello(world)"), True)
    check("unclosed", bracket_validator("((())"), False)
    check("empty string", bracket_validator(""), True)
