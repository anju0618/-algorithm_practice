def hamming_weight(n: int) -> int:
    # TODO: implement (check the lowest bit, then shift right)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", hamming_weight(11), 3)
    check("power of two", hamming_weight(128), 1)
