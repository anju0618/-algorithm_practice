def length_of_lis(nums: list[int]) -> int:
    # tails[i] = 長さi+1の増加部分列を作れる末尾の最小値（patience sorting）
    tails = []

    for n in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < n:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(n)
        else:
            tails[left] = n

    return len(tails)
