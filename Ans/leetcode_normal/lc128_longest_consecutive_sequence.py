def longest_consecutive(nums: list[int]) -> int:
    present = {}  # dictをハッシュ集合の代わりに使う（set()は使わない）
    for n in nums:
        present[n] = True

    longest = 0
    for n in present:
        # nがある連続区間の"先頭"である場合だけ数え始める（O(n)を保つ鍵）
        if n - 1 not in present:
            length = 1
            while n + length in present:
                length += 1
            if length > longest:
                longest = length
    return longest
