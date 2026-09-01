def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    n = len(heights)

    for i in range(n):
        min_height = heights[i]
        left = i
        while left - 1 >= 0 and heights[left - 1] >= min_height:
            left -= 1
        right = i
        while right + 1 < n and heights[right + 1] >= min_height:
            right += 1
        # heights[i] を最小の高さとして、左右にどこまで広げられるかを毎回スキャンする
        area = min_height * (right - left + 1)
        if area > max_area:
            max_area = area

    return max_area
