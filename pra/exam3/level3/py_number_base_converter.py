def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    # TODO: implement without using int(number, base)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("bin to dec", number_base_converter("1010", 2, 10), "10")
    check("hex to dec", number_base_converter("FF", 16, 10), "255")
    check("dec to hex", number_base_converter("255", 10, 16), "FF")
    check("dec to bin", number_base_converter("123", 10, 2), "1111011")
    check("base36 to dec", number_base_converter("Z", 36, 10), "35")
    check("dec to base36", number_base_converter("35", 10, 36), "Z")
    check("invalid from_base", number_base_converter("123", 1, 10), "ERROR")
    check("digit not in base", number_base_converter("G", 16, 10), "ERROR")
