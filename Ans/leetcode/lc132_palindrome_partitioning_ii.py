def min_palindrome_cuts(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [i - 1 for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i):
            sub = s[j:i]
            if sub == sub[::-1]:
                candidate = dp[j] + 1
                if candidate < dp[i]:
                    dp[i] = candidate
    return dp[-1]
