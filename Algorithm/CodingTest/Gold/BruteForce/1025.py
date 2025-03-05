import math

n, m = map(int, input().split(" "))

numbers = []
for _ in range(n):
    digit = input()
    num = [d for d in digit]
    numbers.append(num)

max_num = -1

for r in range(n):
    for c in range(m):
        for dr in range(-n, n):
            for dc in range(-m, m):
                if dr == 0 and dc == 0:
                    continue

                num = ""
                x, y = r, c

                while 0 <= x < n and 0 <= y < m:
                    num += numbers[x][y]
                    value = int(num)

                    is_sqrt = int(math.sqrt(value))

                    if is_sqrt**2 == value:
                        max_num = max(value, max_num)
                    
                    x += dr
                    y += dc

print(max_num)