from typing import Counter

t = int(input())
war = [list(map(int, input().split())) for _ in range(t)]
winner = []

for w in war :
    game = w[0]
    w = sorted(Counter(w[1:]).items())
    has_not_winner = True
    for i in w :
        if i[1] > game // 2 :
            has_not_winner = False
            winner.append(i[0]) 
            break
    if has_not_winner :
        winner.append("SYJKGW")

for w in winner : print(w)    