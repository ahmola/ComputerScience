def solution(sizes):
    w, h = 0, 0
    # 큰 걸 가로로, 작은 걸 세로로
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        w = max(w, size[0])
        h = max(h, size[1])

    return w * h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))