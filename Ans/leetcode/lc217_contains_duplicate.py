def contains_duplicate(nums: list[int]) -> bool:
    seen = {}  # dictをハッシュ集合の代わりに使う（set()は使わない）
    for n in nums:
        if n in seen:
            return True
        seen[n] = True
    return False
