def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for s in strs:
        # 26文字の出現数タプルを"署名"として使う（sorted()は使わない）
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)

        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())
