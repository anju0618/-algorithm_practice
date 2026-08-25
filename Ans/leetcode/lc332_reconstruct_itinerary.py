def find_itinerary(tickets: list[list[str]]) -> list[str]:
    def insertion_sort(arr):
        arr = list(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    graph = {}
    for src, dst in tickets:
        if src not in graph:
            graph[src] = []
        graph[src].append(dst)

    for src in graph:
        graph[src] = insertion_sort(graph[src])  # 辞書順最小を優先的に使うため昇順に

    route = []

    def visit(airport):
        while airport in graph and graph[airport]:
            next_airport = graph[airport].pop(0)
            visit(next_airport)
        route.append(airport)  # Hierholzerのアルゴリズム: 行き止まりから順に記録される

    visit("JFK")

    result = []
    for i in range(len(route) - 1, -1, -1):
        result.append(route[i])
    return result
