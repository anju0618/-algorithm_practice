def check_inclusion(s1: str, s2: str) -> bool:
    # TODO: implement (fixed-size sliding window of char counts)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("permutation present", check_inclusion("ab", "eidbaooo"), True)
    check("no permutation present", check_inclusion("ab", "eidboaoo"), False)
