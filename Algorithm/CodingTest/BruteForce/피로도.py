from itertools import permutations


def solution(k, dungeons):
    answer = -1

    for per in permutations(range(len(dungeons)), len(dungeons)):
        health = k
        count = 0
        for p in per:
            least_health, loss_health = dungeons[p][0], dungeons[p][1]
            if least_health <= health:
                count += 1
                health -= loss_health
            else:
                break
        answer = max(answer, count)

    return answer