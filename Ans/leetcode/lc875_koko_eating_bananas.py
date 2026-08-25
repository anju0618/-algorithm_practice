def min_eating_speed(piles: list[int], h: int) -> int:
    def hours_needed(speed: int) -> int:
        total = 0
        for p in piles:
            total += (p + speed - 1) // speed  # 切り上げ除算
        return total

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid
        else:
            left = mid + 1
    return left
