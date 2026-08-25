def min_distance(word1: str, word2: str) -> int:
    # TODO: implement (classic Levenshtein distance DP)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_distance("horse", "ros"), 3)
    check("longer words", min_distance("intention", "execution"), 5)
