def character_replacement(s: str, k: int) -> int:
    # TODO: implement (sliding window, track most frequent char count)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", character_replacement("ABAB", 2), 4)
    check("replace middle char", character_replacement("AABABBA", 1), 4)
