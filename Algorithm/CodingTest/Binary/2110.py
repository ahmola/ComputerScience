import sys

n, c = map(int, sys.stdin.readline().split())
wifi = list(int(sys.stdin.readline().strip()) for _ in range(n))
wifi.sort()

max_distance = 0
min_dis, max_dis = wifi[1]-wifi[0], wifi[-1]-wifi[0]

while min_dis <= max_dis:
    distance = (min_dis+max_dis)//2
    count = 1
    prev = wifi[0]

    for i in range(1, n):
        if wifi[i] - prev >= distance:
            count += 1
            prev = wifi[i]

    if count >= c:
        min_dis = distance+1
        max_distance = distance
    else:
        max_dis = distance-1
        
print(max_distance)
