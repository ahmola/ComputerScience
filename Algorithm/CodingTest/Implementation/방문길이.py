import sys

def dfs(dirs, x, y, coor):
    for d in dirs:
        nx, ny = x+d[1], y+d[0]
        # 범위 신경쓰자 제발!!!
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            co = [[x, y],[nx, ny]]
            if co not in coor and [co[1], co[0]] not in coor:
                coor.append(co)
            x, y = nx, ny

def solution(dirs):
    dirs = list(dirs)
    coor = []
    for i in range(len(dirs)):
        if dirs[i] == "U":
            dirs[i] = [1,0]
        elif dirs[i] == "D":
            dirs[i] = [-1, 0]
        elif dirs[i] == "R":
            dirs[i] = [0, 1]
        elif dirs[i] == "L":
            dirs[i] = [0, -1]

    dfs(dirs,5, 5, coor)

    return len(coor)

dirs = sys.stdin.readline().strip()
print(solution(dirs))
