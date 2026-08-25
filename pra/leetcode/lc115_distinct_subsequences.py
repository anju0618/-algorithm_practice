def num_distinct(s: str, t: str) -> int:
    # TODO: implement (2D DP: dp[i][j] = ways to form t[:j] from s[:i])
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", num_distinct("rabbbit", "rabbit"), 3)
    check("more matches", num_distinct("babgbag", "bag"), 5)
