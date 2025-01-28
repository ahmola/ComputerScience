year, month, day = map(int, input().split("-"))
n = int(input(""))

total = year * 360 + month * 30 + day + n

year = total // 360
total = total % 360

month = total // 30
if month == 0 :
    month = 12
    year -= 1

total = total % 30
day = total
if day == 0 :
    day = 30
    month -= 1
    if month == 0 :
        month = 12
        year -= 1

if month < 10 :
    month = "0"+str(month)
if day < 10 :
    day = "0"+str(day)

print(f"{year}-{month}-{day}")