def check_valid_string(s: str) -> bool:
    # 開き括弧の数としてありうる範囲 [low, high] を維持する
    low = 0
    high = 0
    for ch in s:
        if ch == "(":
            low += 1
            high += 1
        elif ch == ")":
            low -= 1
            high -= 1
        else:  # '*'
            low -= 1
            high += 1
        if high < 0:
            return False  # '*'を全部'('扱いにしても閉じすぎ
        if low < 0:
            low = 0  # 開き括弧が負にはならない（'*'を空文字扱いにする）
    return low == 0
