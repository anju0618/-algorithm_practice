def word_break(s: str, word_dict: list[str]) -> bool:
    # TODO: implement (DP: dp[i] = can the first i characters be segmented)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", word_break("leetcode", ["leet", "code"]), True)
    check("reused word", word_break("applepenapple", ["apple", "pen"]), True)
    check("not segmentable", word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
