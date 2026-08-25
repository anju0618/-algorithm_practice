def least_interval(tasks: list[str], n: int) -> int:
    counts = {}
    for t in tasks:
        counts[t] = counts.get(t, 0) + 1

    max_count = 0
    for c in counts.values():
        if c > max_count:
            max_count = c

    max_count_tasks = 0
    for c in counts.values():
        if c == max_count:
            max_count_tasks += 1

    # 最頻出タスクを軸に (max_count-1) 個の「幅n+1のブロック」を作り、
    # 最後に同率最頻出タスクをまとめて並べる、という下限の式
    formula = (max_count - 1) * (n + 1) + max_count_tasks
    return max(len(tasks), formula)
