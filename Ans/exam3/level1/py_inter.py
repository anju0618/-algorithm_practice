def inter(s1: str, s2: str) -> str:
    result = []
    seen = []
    for ch in s1:
        # `in` を素のリストに対する線形探索として使う（set()は使わない）
        if ch in s2 and ch not in seen:
            result.append(ch)
            seen.append(ch)
    return "".join(result)
