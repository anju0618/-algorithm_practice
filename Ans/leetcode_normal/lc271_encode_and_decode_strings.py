def encode(strs: list[str]) -> str:
    # 各文字列の前に "長さ#" を付ける（長さをヘッダにすることで、
    # 文字列の中身にどんな文字が入っていても安全に区切れる）
    parts = []
    for s in strs:
        parts.append(str(len(s)) + "#" + s)
    return "".join(parts)


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        start = j + 1
        result.append(s[start:start + length])
        i = start + length
    return result
