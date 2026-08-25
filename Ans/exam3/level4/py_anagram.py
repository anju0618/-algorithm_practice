def anagram(s1: str, s2: str) -> bool:
    cleaned_s1 = s1.replace(" ", "").lower()
    cleaned_s2 = s2.replace(" ", "").lower()
    if len(cleaned_s1) != len(cleaned_s2):
        return False

    counts = {}
    for ch in cleaned_s1:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in cleaned_s2:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    for v in counts.values():
        if v != 0:
            return False
    return True
