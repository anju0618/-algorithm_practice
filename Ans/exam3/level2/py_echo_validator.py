def echo_validator(text: str) -> bool:
    if not text:
        return False

    cleaned = []
    for ch in text.lower():
        if ch.isalpha():
            cleaned.append(ch)

    if not cleaned:
        return False

    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            return False
    return True
