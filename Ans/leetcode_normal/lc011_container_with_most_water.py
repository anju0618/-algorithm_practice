def max_area(height: list[int]) -> int:
    best = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            h = height[i] if height[i] < height[j] else height[j]
            area = h * (j - i)
            if area > best:
                best = area
    return best
