def reverse(x: int) -> int:
    # TODO: implement (peel off digits with % and //, rebuild in reverse, check 32-bit overflow)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("positive", reverse(123), 321)
    check("negative", reverse(-123), -321)
    check("trailing zero dropped", reverse(120), 21)
