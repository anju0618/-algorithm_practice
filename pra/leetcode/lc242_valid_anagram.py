def is_anagram(s: str, t: str) -> bool:
    # TODO: implement without sorted()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic anagram", is_anagram("anagram", "nagaram"), True)
    check("not an anagram", is_anagram("rat", "car"), False)
