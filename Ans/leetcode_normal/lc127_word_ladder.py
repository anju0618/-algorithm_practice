def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    word_set = {}
    for w in word_list:
        word_set[w] = True
    if end_word not in word_set:
        return 0

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    queue = [(begin_word, 1)]
    visited = {begin_word: True}

    head = 0
    while head < len(queue):
        word, steps = queue[head]
        head += 1
        if word == end_word:
            return steps
        for i in range(len(word)):
            for ch in alphabet:
                if ch == word[i]:
                    continue
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in word_set and candidate not in visited:
                    visited[candidate] = True
                    queue.append((candidate, steps + 1))
    return 0
