def is_subsequence(s: str, t: str) -> bool:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("valid subsequence", is_subsequence("abc", "ahbgdc"), True)
    check("not a subsequence", is_subsequence("axc", "ahbgdc"), False)
