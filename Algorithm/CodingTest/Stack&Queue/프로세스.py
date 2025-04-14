from collections import deque


def solution(priorities, location):
    execute = deque([i for i in range(len(priorities))])
    priority = [0] * len(priorities)
    p = 1
    while execute:
        target = max(priorities)
        behind = priorities.pop(0)
        if priorities[0] < target:
            priorities.append(behind)
            execute.rotate(-1)
        else:
            priority[execute.popleft()] = p
            p += 1
    print(priority)
    return priority[location]
print(solution([1, 1, 9, 1, 1, 1], 0))