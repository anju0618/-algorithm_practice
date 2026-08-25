def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    start = 0
    best = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        length = i - start + 1
        if length > best:
            best = length
    return best
