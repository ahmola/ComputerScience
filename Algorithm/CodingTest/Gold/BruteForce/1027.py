def find_inc(target, inc):
    how_many = 0

    # 첫번째 건물은 무조건 보임
    # 왼쪽에서는 기울기 감소
    min_slope = None
    for i in range(target-1, -1, -1):
        slope = (inc[i]-inc[target])/(i-target)
        if min_slope == None or min_slope > slope:
            how_many += 1
            min_slope = slope

    # 오른쪽에서는 기울기 증가
    max_slope = None
    for i in range(target+1, len(inc)):
        slope = (inc[target]-inc[i])/(target-i)
        if max_slope == None or max_slope < slope:
            how_many += 1
            max_slope = slope

    return how_many

n = int(input())
building = list(map(int, input().split(" ")))

how_many = []
for i in range(n):
    how_many.append(find_inc(i, building))

print(max(how_many))