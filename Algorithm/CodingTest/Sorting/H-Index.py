def solution(citations):
    citations.sort()
    leng = len(citations)

    for i in range(leng):
        h = leng - i
        if citations[i] >= h:
            return h
    return 0