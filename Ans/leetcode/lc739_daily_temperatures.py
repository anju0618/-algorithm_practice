def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # まだ「もっと暖かい日」を待っているインデックス（気温は下から上に単調減少）

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
