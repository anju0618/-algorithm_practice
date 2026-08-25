def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n  # 同じ数を2回XORすると0に戻るので、ペアが全部消えて1つだけ残る
    return result
