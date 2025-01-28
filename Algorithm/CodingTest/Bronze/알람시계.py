h, m = map(int, input().split())

total = h * 60 + m - 45

if total < 0 :
    total += 60 * 24 

h = total // 60
total = total % 60
if h >= 24 :
    h -= 24

m = total
if m >= 60 :
    m -= 60

print(f"{h} {m}")