def whisper_cipher(text: str, shift: int) -> str:
    if not text:
        return ""

    result = []
    for ch in text:
        if ch.isupper():
            base = ord("A")
            new_pos = (ord(ch) - base + shift) % 26
            result.append(chr(base + new_pos))
        elif ch.islower():
            base = ord("a")
            new_pos = (ord(ch) - base + shift) % 26
            result.append(chr(base + new_pos))
        else:
            result.append(ch)
    return "".join(result)
