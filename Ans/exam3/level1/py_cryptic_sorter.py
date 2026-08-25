def cryptic_sorter(strings: list[str]) -> list[str]:
    vowels = "aeiou"

    def vowel_count(s: str) -> int:
        count = 0
        for ch in s:
            if ch in vowels:
                count += 1
        return count

    def less_than(a: str, b: str) -> bool:
        # 1) 短い方が先
        if len(a) != len(b):
            return len(a) < len(b)
        # 2) 大文字小文字を無視したASCII順
        la, lb = a.lower(), b.lower()
        if la != lb:
            return la < lb
        # 3) 元の文字列そのもの（大文字/小文字の違いをここで区別）
        if a != b:
            return a < b
        # 4) 完全に同じ文字列同士なら母音数（実質使われないが仕様通り実装）
        return vowel_count(a) < vowel_count(b)

    result = list(strings)
    # 挿入ソート（安定ソート）を手書きし、sorted()/.sort()を使わない
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and less_than(key, result[j]):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result
