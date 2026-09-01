def is_happy(n: int) -> bool:
    seen = {}
    while n != 1 and n not in seen:
        seen[n] = True
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        n = total
    return n == 1
