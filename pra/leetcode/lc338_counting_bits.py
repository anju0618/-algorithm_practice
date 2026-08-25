def count_bits(n: int) -> list[int]:
    # TODO: implement (DP: ans[i] = ans[i >> 1] + (i & 1))
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("n=2", count_bits(2), [0, 1, 1])
    check("n=5", count_bits(5), [0, 1, 1, 2, 1, 2])
