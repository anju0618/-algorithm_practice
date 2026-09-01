def max_coins(nums: list[int]) -> int:
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]

    # length = 区間(left, right)の開いた区間の幅。最後に破裂させる風船kを軸に考える
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right] + dp[left][k] + dp[k][right]
                if coins > dp[left][right]:
                    dp[left][right] = coins

    return dp[0][n - 1]
