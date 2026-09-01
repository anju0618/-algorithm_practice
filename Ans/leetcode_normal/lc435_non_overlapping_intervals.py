def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    def insertion_sort(arr):
        arr = list(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j][1] > key[1]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    intervals = insertion_sort(intervals)  # 終了時刻の昇順に並べる（区間スケジューリングの定石）
    count = 0
    prev_end = float("-inf")

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            count += 1  # 重なっているので、このintervalを消す扱いにする

    return count
