def dfs(start, graph, visited):
    visited[start] = True
    count = 1
    for node in graph[start]:
        if not visited[node]:
            count += dfs(node, graph, visited)
    return count


def solution(n, wires):
    answer = n

    for cut in wires:
        virtual = {i: [] for i in range(1, n + 1)}
        for wire in wires:
            a, b = wire[0], wire[1]
            if [a, b] == cut or [b, a] == cut:
                continue
            virtual[a] = b
            virtual[b] = a

        visited = [False] * (n + 1)
        side = dfs(1, virtual, visited)
        other = n - side
        answer = min(answer, abs(side - other))

    return answer
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))