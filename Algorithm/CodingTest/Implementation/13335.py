import sys
from collections import deque

n, l, w = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
truck = deque(truck)
time = 1
bridge = deque()
bridge.append(truck.popleft())

while truck:
    if len(bridge) == l:
        bridge.popleft()

    if truck and sum(bridge)+truck[0] <= w:
        bridge.append(truck.popleft())
    else:
        bridge.append(0)
    time += 1

print(time+l)