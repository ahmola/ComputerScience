def is_yoon(year) :
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    return 365

def day_in_month(year, month) :
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_yoon(year) == 366 :
        return 29
    return day[month-1]

sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

if ey - sy > 1000 or (ey - sy == 1000 and em > sm) or (ey - sy == 1000 and em == sm and ed >= sd):
    print("gg")
else :
    day = 0
    # 년
    for i in range(sy+1, ey) :
        day += is_yoon(i)
    # 월(년도가 다를 때)
    if ey > sy :
        # 금년
        for i in range(sm+1, 13) :
            day += day_in_month(sy, i)
        day += (day_in_month(sy, sm) - sd)
        # 내년
        for i in range(1, em) :
            day += day_in_month(ey, i)
        day += ed
    # 월(년도가 같을 때)
    else :
        for i in range(sm+1, em) :
            day += day_in_month(sy, i)
        day += (day_in_month(sy, sm) - sd)
        day += ed
    print(f"D-{day}")
