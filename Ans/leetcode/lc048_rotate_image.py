def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # 転置する
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 各行を左右反転する（転置＋左右反転＝時計回り90度回転）
    for row in matrix:
        left, right = 0, n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
