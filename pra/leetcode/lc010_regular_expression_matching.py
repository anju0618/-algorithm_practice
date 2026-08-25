def is_match(s: str, p: str) -> bool:
    # TODO: implement (2D DP over s and p, handling '.' and '*')
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("no match", is_match("aa", "a"), False)
    check("star repeats", is_match("aa", "a*"), True)
    check("dot star matches anything", is_match("ab", ".*"), True)
