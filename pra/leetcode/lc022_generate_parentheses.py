def generate_parenthesis(n: int) -> list[str]:
    # TODO: implement (backtracking, track open/close counts used)
    pass


def check(label, actual, expected):
    ok = sorted(actual) == sorted(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("n=3", generate_parenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
    check("n=1", generate_parenthesis(1), ["()"])
