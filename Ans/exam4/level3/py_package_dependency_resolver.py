def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    def insertion_sort(items: list[str]) -> list[str]:
        # アルファベット順に並べる（sorted()/.sort()は使わない）
        arr = list(items)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # graph[dep]には「depを待っている側」、in_degree[name]には「まだ残っている依存の数」を入れる
    graph = {name: [] for name in packages}
    in_degree = {name: 0 for name in packages}
    for name, deps in packages.items():
        for dep in deps:
            if dep in packages:
                graph[dep].append(name)
                in_degree[name] += 1

    ready = []
    for name in packages:
        if in_degree[name] == 0:
            ready.append(name)
    ready = insertion_sort(ready)

    result = []
    while ready:
        next_ready = []
        for name in ready:
            result.append(name)
            for neighbor in graph[name]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    next_ready.append(neighbor)
        ready = insertion_sort(next_ready)

    if len(result) != len(packages):
        return []
    return result
