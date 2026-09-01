def search_matrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        val = matrix[row][col]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
