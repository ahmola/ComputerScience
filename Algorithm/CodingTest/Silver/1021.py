from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))

queue = deque(range(1, n+1))

move_count = 0

for t in target :
    index= queue.index(t)

    if index <= len(queue) // 2 : # 찾고자 하는 인덱스가 큐의 중간 인덱스보다 작아서 왼쪽으로 옮기는게 빠른 경우
        queue.rotate(-index) # 왼쪽으로 인덱스만큼 움직임
        move_count += index
    else : # 큐의 중간 인덱스보다 커서 오른쪽으로 옮기는게 빠른 경우
        queue.rotate(+(len(queue)-index)) # 오른쪽으로 인덱스만큼 움직임
        move_count += len(queue) - index

    queue.popleft() # 맨 처음 원소를 제거

print(move_count)