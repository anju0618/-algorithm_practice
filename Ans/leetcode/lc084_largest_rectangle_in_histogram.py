def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # (開始インデックス, 高さ) のペア。高さは単調増加
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            area = height * (i - idx)
            if area > max_area:
                max_area = area
            start = idx
        stack.append((start, h))

    n = len(heights)
    for idx, height in stack:
        area = height * (n - idx)
        if area > max_area:
            max_area = area
    return max_area
