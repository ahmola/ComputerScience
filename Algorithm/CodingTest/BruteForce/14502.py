from itertools import combinations

def spread(lab, n, m):
    location = []

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                location.append([i, j])

    for l in location:
        i,j = l[0],l[1]
        for p in range(j+1, m):
            if lab[i][p] != 0:
                break
            lab[i][p] = 2
            location.append([i, p])
        for q in range(i-1, -1, -1):
            if lab[q][j] != 0:
                break
            lab[q][j] = 2
            location.append([q, j])
        for r in range(j-1, -1, -1):
            if lab[i][r] != 0:
                break
            lab[i][r] = 2
            location.append([i, r])
        for s in range(i+1, n):
            if lab[s][j] != 0:
                break
            lab[s][j] = 2
            location.append([s, j])
    
def baricade(lab, wall):
    for w in wall:
        lab[w[0]][w[1]] = 1

def virus(lab, n, m):
    max_safe = 0
    # 바리케이드를 칠 수 있는 후보지를 찾음
    expect = [[i, j] for i in range(n) for j in range(m) if lab[i][j] == 0]

    for ex in combinations(expect, 3):
        # deepcopy보다 이게 행을 통째로 배껴서 반복문으로 삽입하는게 빠름
        copy_lab = [row[:] for row in lab]
        ex = list(ex)
        safe = 0
        # 바리케이드를 침
        baricade(copy_lab, ex)
        # 바이러스가 퍼짐
        spread(copy_lab, n, m)
        # 퍼진 뒤에 안전구역 셈
        safe = sum(row.count(0) for row in copy_lab)
        # 최댓값 판별
        max_safe = max(max_safe, safe)

    return max_safe
    
n, m = map(int, input().split(" "))
lab = [list(map(int, input().split(" "))) for _ in range(n)]

print(virus(lab,n,m))