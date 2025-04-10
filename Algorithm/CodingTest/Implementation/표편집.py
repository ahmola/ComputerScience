from collections import deque

def solution(n, k, cmd):
    cmd = [list(map(str, c.split())) for c in cmd]
    answer = ["O"]*n
    cache = deque()
    index = k

    for c in cmd:
        if c[0] == "U":
            i = 0
            while i < int(c[1]):
                index -= 1
                if answer[index] == "O":
                    i += 1

        elif c[0] == "D":
            i = 0
            while i < int(c[1]):
                index += 1
                if answer[index] == "O":
                    i += 1

        elif c[0] == "C":
            answer[index] = "X"
            cache.append(index)
            if index == n-1:
                index -= 1
            else:
                index += 1

        elif c[0] == "Z":
            last = cache.pop()
            answer[last] = "O"

        print(index, c, cache, answer)

    return "".join(answer)