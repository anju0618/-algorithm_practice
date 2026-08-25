def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True

    s_i = 0
    s_len = len(s)
    for ch in t:
        if ch == s[s_i]:
            s_i += 1
            if s_i == s_len:
                return True
    return False
