def find_target_sum_ways(nums: list[int], target: int) -> int:
    ways = {0: 1}  # 部分和 -> その和を作る方法の数
    for n in nums:
        next_ways = {}
        for total, count in ways.items():
            next_ways[total + n] = next_ways.get(total + n, 0) + count
            next_ways[total - n] = next_ways.get(total - n, 0) + count
        ways = next_ways
    return ways.get(target, 0)
