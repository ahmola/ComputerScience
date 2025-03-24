import sys

n = int(sys.stdin.readline().strip())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
times.sort(key=lambda x : (x[1], x[0]))

end_time = 0
count = 0

for start, end in times:
    if start >= end_time:
        end_time = end
        count += 1

print(count)