import sys

def looper(diction, msg):
    index = 27
    result = []
    i = 0
    while i < len(msg):
        word = msg[i]
        i += 1
        while i < len(msg) and word+msg[i] in diction:
            word += msg[i]
            i += 1
        if i < len(msg):
            diction[word+msg[i]] = index
            index += 1
        result.append(diction[word])
    # print(diction)
    return result

def solution(msg):
    msg = list(msg)
    diction = {}
    for i in range(65, 91):
        diction[chr(i)] = i-64
    return looper(diction, msg)

msg = sys.stdin.readline().strip()
print(solution(msg))