from collections import deque


def count_diff(word, target):
    count = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            count += 1
    return count


def solution(begin, target, words):
    if target not in words:
        return 0
    words = [begin] + words
    queue = deque()
    visited = [0] * len(words)
    queue.append(begin)
    while queue:
        print(queue)
        word = queue.popleft()

        for i in range(len(words)):
            if word != words[i] and visited[i] == 0 and count_diff(word, words[i]) == 1:
                visited[i] = visited[words.index(word)]+1
                queue.append(words[i])
    return visited[words.index(target)]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))