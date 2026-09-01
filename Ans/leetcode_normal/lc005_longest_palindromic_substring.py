def longest_palindrome(s: str) -> str:
    def is_palindrome(sub: str) -> bool:
        left, right = 0, len(sub) - 1
        while left < right:
            if sub[left] != sub[right]:
                return False
            left += 1
            right -= 1
        return True

    best = ""
    for start in range(len(s)):
        for end in range(start, len(s)):
            candidate = s[start:end + 1]
            if len(candidate) > len(best) and is_palindrome(candidate):
                best = candidate
    return best
