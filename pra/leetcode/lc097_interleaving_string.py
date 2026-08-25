def is_interleave(s1: str, s2: str, s3: str) -> bool:
    # TODO: implement (2D DP: dp[i][j] = can s3[:i+j] be formed from s1[:i] and s2[:j])
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("valid interleaving", is_interleave("aabcc", "dbbca", "aadbbcbcac"), True)
    check("invalid interleaving", is_interleave("aabcc", "dbbca", "aadbbbaccc"), False)
    check("all empty", is_interleave("", "", ""), True)
