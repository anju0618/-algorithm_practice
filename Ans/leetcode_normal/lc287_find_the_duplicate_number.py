def find_duplicate(nums: list[int]) -> int:
    # setは禁止なので、見た値をdictに記録しながら線形に見ていくだけ
    seen = {}
    for x in nums:
        if x in seen:
            return x
        seen[x] = True
    return -1
