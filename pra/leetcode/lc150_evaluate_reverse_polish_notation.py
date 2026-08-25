def eval_rpn(tokens: list[str]) -> int:
    # TODO: implement with a stack
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", eval_rpn(["2", "1", "+", "3", "*"]), 9)
    check("with division", eval_rpn(["4", "13", "5", "/", "+"]), 6)
    check("complex expression", eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
