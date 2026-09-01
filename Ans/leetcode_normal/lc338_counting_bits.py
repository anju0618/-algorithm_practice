def count_bits(n: int) -> list[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        # iを1ビット右シフトしたものはすでに計算済み。最後のビットを足すだけ
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
