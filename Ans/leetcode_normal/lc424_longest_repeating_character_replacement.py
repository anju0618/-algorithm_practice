def character_replacement(s: str, k: int) -> int:
    counts = {}
    start = 0
    max_count = 0
    best = 0

    for end in range(len(s)):
        ch = s[end]
        counts[ch] = counts.get(ch, 0) + 1
        if counts[ch] > max_count:
            max_count = counts[ch]

        window_len = end - start + 1
        if window_len - max_count > k:
            left_ch = s[start]
            counts[left_ch] -= 1
            start += 1

        window_len = end - start + 1
        if window_len > best:
            best = window_len
    return best
