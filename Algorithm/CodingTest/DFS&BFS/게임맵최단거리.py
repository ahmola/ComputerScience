from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for move in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

    return visited[n - 1][m - 1] if visited[n - 1][m - 1] != 0 else -1