def find_kth_largest(nums: list[int], k: int) -> int:
    arr = list(nums)
    val = None
    for _ in range(k):
        max_i = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_i]:
                max_i = i
        val = arr.pop(max_i)
    return val
