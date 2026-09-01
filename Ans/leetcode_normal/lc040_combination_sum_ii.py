def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    def insertion_sort(arr):
        arr = list(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    candidates = insertion_sort(candidates)
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # 同じ深さで同じ値を2回試さない（重複組み合わせを避ける）
            if candidates[i] > remaining:
                break  # ソート済みなのでこれ以降も全部超過
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return result
