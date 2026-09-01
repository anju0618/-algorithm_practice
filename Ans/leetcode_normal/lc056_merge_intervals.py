def merge(intervals: list[list[int]]) -> list[list[int]]:
    def insertion_sort(arr):
        arr = list(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j][0] > key[0]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    intervals = insertion_sort(intervals)
    result = [list(intervals[0])]

    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            if end > last[1]:
                last[1] = end
        else:
            result.append([start, end])

    return result
