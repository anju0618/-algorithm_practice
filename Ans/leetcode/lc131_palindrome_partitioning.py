def partition(s: str) -> list[list[str]]:
    result = []
    path = []

    def is_palindrome(sub: str) -> bool:
        n = len(sub)
        for i in range(n // 2):
            if sub[i] != sub[n - 1 - i]:
                return False
        return True

    def backtrack(start):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if is_palindrome(sub):
                path.append(sub)
                backtrack(end)
                path.pop()

    backtrack(0)
    return result
