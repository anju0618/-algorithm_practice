def rotate_string(s: str, goal: str) -> bool:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("valid rotation", rotate_string("abcde", "cdeab"), True)
    check("not a rotation", rotate_string("abcde", "abced"), False)
