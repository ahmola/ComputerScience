def solution(genres, plays):
    answer = []
    rank = {}
    for g in set(genres):
        rank[g] = []

    for i in range(len(plays)):
        rank[genres[i]].append([i, plays[i]])

    rank = [rank[genre] for genre in rank]
    for genre in rank:
        total = 0
        for play in genre:
            total += play[1]
        genre.sort(key=lambda x:x[1], reverse=True)
        genre.append(total)
    rank.sort(key=lambda x : x[-1],reverse=True)

    for genre in rank:
        if len(genre) >= 3:
            answer.append([genre[0][0], genre[1][0]])
        else:
            answer.append([genre[0][0]])

    return sum(answer,[])

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))