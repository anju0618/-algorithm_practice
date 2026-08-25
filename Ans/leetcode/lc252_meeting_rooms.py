def can_attend_meetings(intervals: list[list[int]]) -> bool:
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
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
