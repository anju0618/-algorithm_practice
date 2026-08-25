def course_order(courses: dict[str, list[str]]) -> list[str]:
    if not courses:
        return []

    graph = {name: [] for name in courses}
    in_degree = {name: 0 for name in courses}
    for name, prereqs in courses.items():
        for p in prereqs:
            if p in courses:
                graph[p].append(name)
                in_degree[name] += 1

    queue = []
    for name in courses:
        if in_degree[name] == 0:
            queue.append(name)

    result = []
    head = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(courses):
        return []
    return result
