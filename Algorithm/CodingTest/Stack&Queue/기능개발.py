def solution(progresses, speeds):
    answer = [0] * len(speeds)

    day = 1
    while any(progress < 100 for progress in progresses):
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                continue
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                answer[i] = day
        day += 1

    result = []
    i, j = 0, 1
    while j < len(answer):
        print(j)
        commit = 1
        while j < len(answer) and answer[j] <= answer[i]:
            commit += 1
            j += 1
        result.append(commit)
        i = j
        j += 1

    if j == len(answer):
        result.append(1)

    return result

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))