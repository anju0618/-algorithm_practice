def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True

    n = len(arr1)
    for start in range(n):
        match = True
        for i in range(n):
            if arr1[(start + i) % n] != arr2[i]:
                match = False
                break
        if match:
            return True
    return False
