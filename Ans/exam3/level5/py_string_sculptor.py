def string_sculptor(text: str) -> str:
    if not text:
        return ""
    result = []
    upper_next = False
    for ch in text:
        if ch == " ":
            upper_next = False
            result.append(ch)
        elif ch.isalpha():
            if upper_next:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
            upper_next = not upper_next
        else:
            result.append(ch)
    return "".join(result)
