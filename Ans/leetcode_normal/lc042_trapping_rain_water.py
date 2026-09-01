def trap(height: list[int]) -> int:
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    running = 0
    for i in range(n):
        if height[i] > running:
            running = height[i]
        left_max[i] = running

    right_max = [0] * n
    running = 0
    for i in range(n - 1, -1, -1):
        if height[i] > running:
            running = height[i]
        right_max[i] = running

    water = 0
    for i in range(n):
        bound = left_max[i] if left_max[i] < right_max[i] else right_max[i]
        water += bound - height[i]
    return water
