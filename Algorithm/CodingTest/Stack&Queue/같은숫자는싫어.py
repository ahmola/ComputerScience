from collections import deque

def solution(arr):
    answer = deque()
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
            continue

        last = answer.pop()
        if last != arr[i]:
            answer.append(last)
            answer.append(arr[i])
        else:
            answer.append(last)

    return list(answer)