def encode(strs: list[str]) -> str:
    # TODO: implement (length-prefix encoding)
    pass


def decode(s: str) -> list[str]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", decode(encode(["lint", "code", "love", "you"])), ["lint", "code", "love", "you"])
    check("with delimiter-like chars", decode(encode(["we", "say", ":", "yes"])), ["we", "say", ":", "yes"])
    check("empty list", decode(encode([])), [])
