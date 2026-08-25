def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask

    if a > 0x7FFFFFFF:
        # 32bit符号付き整数として負の値を表す場合の変換
        return ~(a ^ mask)
    return a
