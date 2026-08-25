def min_meeting_rooms(intervals: list[list[int]]) -> int:
    def insertion_sort(values):
        arr = list(values)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    starts = insertion_sort(iv[0] for iv in intervals)
    ends = insertion_sort(iv[1] for iv in intervals)

    rooms = 0
    max_rooms = 0
    s = e = 0
    n = len(intervals)

    while s < n:
        if starts[s] < ends[e]:
            rooms += 1
            if rooms > max_rooms:
                max_rooms = rooms
            s += 1
        else:
            rooms -= 1
            e += 1

    return max_rooms
