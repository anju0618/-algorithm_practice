def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)

    window = {}
    formed = 0
    left = 0
    best_len = -1
    best_left = 0

    for right, ch in enumerate(s):
        if ch in need:
            window[ch] = window.get(ch, 0) + 1
            if window[ch] == need[ch]:
                formed += 1

        while formed == required:
            if best_len == -1 or right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left

            left_ch = s[left]
            if left_ch in need:
                window[left_ch] -= 1
                if window[left_ch] < need[left_ch]:
                    formed -= 1
            left += 1

    if best_len == -1:
        return ""
    return s[best_left:best_left + best_len]
