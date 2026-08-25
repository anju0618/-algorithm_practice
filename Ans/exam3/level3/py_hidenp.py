def hidenp(small: str, big: str) -> bool:
    if not small:
        return True

    s_i = 0
    small_len = len(small)

    for ch in big:
        if ch == small[s_i]:
            s_i += 1
            if s_i == small_len:
                return True
    return False
