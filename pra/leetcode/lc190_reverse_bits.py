def reverse_bits(n: int) -> int:
    # TODO: implement (shift 32 bits from n into result, one at a time)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", reverse_bits(43261596), 964176192)
    check("near max", reverse_bits(2147483644), 1073741822)
