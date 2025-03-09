from itertools import combinations

def sum_of_team(team, synergy):
    s = 0

    for i in team:
        for j in team:
            if i is not j:
                s += synergy[i][j]
    
    return s

def team(synergy, n):
    min_synergy = float('Inf')

    for team_a in combinations(range(n), n//2):
        team_a = list(team_a)
        team_b = []
        for s in range(n):
            if s not in team_a:
                team_b.append(s)

        s_a = sum_of_team(team_a, synergy)
        s_b = sum_of_team(team_b, synergy)
        
        if abs(s_a - s_b) < min_synergy:
            min_synergy = abs(s_a-s_b)

    return min_synergy

n = int(input())
synergy = [list(map(int, input().split(" "))) for _ in range(n)]

print(team(synergy, n))