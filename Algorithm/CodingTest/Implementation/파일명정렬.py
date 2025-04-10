import sys

def solution(files):
    length = len(files)
    priority = [[] for _ in range(length)]

    for i in range(length):
        head = ""
        index = 0
        while index < len(files[i]):
            if files[i][index].isdigit():
                break
            head += files[i][index]
            index += 1
        priority[i].append(head.lower())

        number = ""
        while index < len(files[i]):
            if files[i][index].isdigit():
                number += files[i][index]
                index += 1
            else:
                break
        priority[i].append(int(number))

        priority[i].append(i)

    priority.sort()
    result = []
    for p in priority:
        result.append(files[p[2]])

    return result

files = list(sys.stdin.readline().split())
print(solution(files))