month = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_yoon(year) :
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

m, d, y, t = input().split()

y = int(y)
d = int(d[:-1])
hour, minute = map(int, t.split(":"))

# 윤년 판별
year_to_min = 1
if is_yoon(y) :
    days[1] = 29
    year_to_min = 366 * 24 * 60 
else :
    year_to_min = 365 * 24 * 60

# 분으로 맞춤. 분+시간+날
times = minute + hour*60 + (d-1)*24*60

# 지금까지 지난 달을 계산
for i in range(month[m]-1) :
    times += days[i] * 24 * 60

print(f"{100*(times/year_to_min)}")