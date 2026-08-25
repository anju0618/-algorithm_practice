def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    n = len(arr)
    real_k = k % n
    if real_k == 0:
        return arr[:]

    result = []
    for i in range(n - real_k, n):
        result.append(arr[i])
    for i in range(0, n - real_k):
        result.append(arr[i])
    return result
