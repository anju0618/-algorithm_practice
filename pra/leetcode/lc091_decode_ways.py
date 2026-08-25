def num_decodings(s: str) -> int:
    # TODO: implement (DP: dp[i] = ways to decode the first i characters)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", num_decodings("12"), 2)
    check("three groupings", num_decodings("226"), 3)
    check("invalid leading zero", num_decodings("06"), 0)
