def plus_one(digits: list[int]) -> list[int]:
    result = digits[:]
    i = len(result) - 1

    while i >= 0:
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0
        i -= 1

    return [1] + result  # 全部繰り上がった場合（999 -> 1000）
