def length_of_longest_substring(s: str) -> int:
    best = 0
    for start in range(len(s)):
        seen = []
        for end in range(start, len(s)):
            if s[end] in seen:
                break
            seen.append(s[end])
        if len(seen) > best:
            best = len(seen)
    return best
