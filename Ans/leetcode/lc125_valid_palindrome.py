def is_valid_palindrome(s: str) -> bool:
    cleaned = []
    for ch in s.lower():
        if ch.isalnum():
            cleaned.append(ch)

    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            return False
    return True
