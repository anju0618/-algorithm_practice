def echo_validator(text: str) -> bool:
    # TODO: 実装する（アルファベット以外は無視、大文字小文字も無視）
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple palindrome", echo_validator("racecar"), True)
    check("sentence palindrome", echo_validator("A man a plan a canal Panama"), True)
    check("not a palindrome", echo_validator("race a car"), False)
    check("with punctuation-like spacing", echo_validator("Was it a car or a cat I saw"), True)
    check("plain word", echo_validator("hello"), False)
    check("mixed case", echo_validator("Madam Im Adam"), True)
    check("empty string", echo_validator(""), False)
