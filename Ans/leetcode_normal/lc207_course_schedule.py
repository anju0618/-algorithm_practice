def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    queue = []
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    finished = 0
    head = 0
    while head < len(queue):
        curr = queue[head]
        head += 1
        finished += 1
        for nxt in graph[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return finished == num_courses
