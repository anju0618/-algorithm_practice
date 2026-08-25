def unique_paths(m: int, n: int) -> int:
    # TODO: implement (DP, dp[j] += dp[j-1] row by row)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("3x7", unique_paths(3, 7), 28)
    check("3x2", unique_paths(3, 2), 3)
