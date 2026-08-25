def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    counts = {}
    for ch in s1:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in s2:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    for v in counts.values():
        if v != 0:
            return False
    return True
