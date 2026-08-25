def whisper_cipher(text: str, shift: int) -> str:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic shift", whisper_cipher("hello", 3), "khoor")
    check("preserves case and punctuation", whisper_cipher("Hello World!", 1), "Ifmmp Xpsme!")
    check("wraps around z", whisper_cipher("xyz", 3), "abc")
    check("digits unchanged", whisper_cipher("ABC123def", 5), "FGH123ijk")
    check("empty string", whisper_cipher("", 10), "")
    check("negative shift", whisper_cipher("abc", -3), "xyz")
