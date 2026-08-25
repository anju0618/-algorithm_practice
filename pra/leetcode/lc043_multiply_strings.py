def multiply(num1: str, num2: str) -> str:
    # TODO: implement (grade-school long multiplication into a fixed-size digit array)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("single digits", multiply("2", "3"), "6")
    check("multi-digit", multiply("123", "456"), "56088")
