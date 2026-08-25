def alien_order(words: list[str]) -> str:
    graph = {}
    in_degree = {}
    for w in words:
        for ch in w:
            if ch not in graph:
                graph[ch] = []
                in_degree[ch] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = len(w1) if len(w1) < len(w2) else len(w2)
        found_diff = False
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                in_degree[w2[j]] += 1
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            return ""  # 長い単語が短いプレフィックスより前に来るのは矛盾

    queue = []
    for ch in in_degree:
        if in_degree[ch] == 0:
            queue.append(ch)

    result = []
    head = 0
    while head < len(queue):
        ch = queue[head]
        head += 1
        result.append(ch)
        for nxt in graph[ch]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(result) != len(in_degree):
        return ""  # 全文字を並べきれなかった = サイクルがある
    return "".join(result)
