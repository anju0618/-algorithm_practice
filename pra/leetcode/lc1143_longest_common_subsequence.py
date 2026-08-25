def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO: implement (classic 2D LCS DP table)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", longest_common_subsequence("abcde", "ace"), 3)
    check("no common subsequence", longest_common_subsequence("abc", "def"), 0)
