def hamming_weight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
