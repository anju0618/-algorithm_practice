def check_inclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False

    need = [0] * 26
    for ch in s1:
        need[ord(ch) - ord("a")] += 1

    for start in range(n2 - n1 + 1):
        window = [0] * 26
        for i in range(start, start + n1):
            window[ord(s2[i]) - ord("a")] += 1
        if window == need:
            return True
    return False
