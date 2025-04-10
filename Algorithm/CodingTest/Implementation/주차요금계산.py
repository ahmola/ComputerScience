def solution(fees, records):
    records = [list(map(str, car.split())) for car in records]
    records.sort(key= lambda car: car[1])
    result = {}
    for r in records:
        if r[1] not in result:
            result[r[1]] = 0

    for record in records:
        if record[2] == 'IN':
            index = records.index(record)
            spend = 0
            is_not_out = True
            in_time = record[0]
            in_time_hour, in_time_minute = map(int, in_time.split(":"))
            for i in range(index+1, len(records)): # 나간 시간을 계산
                if records[i][1] == record[1] and records[i][2] == 'OUT':
                    is_not_out = False
                    out_time = records[i][0]
                    out_time_hour, out_time_minute = map(int, out_time.split(":"))
                    spend = (out_time_hour-in_time_hour)*60 + (out_time_minute-in_time_minute)
                    break

            if is_not_out: # 나가지 않았다면
                spend = (23-in_time_hour)*60 + (59-in_time_minute)

            result[record[1]] += spend

    for r in result:
        if result[r] <= fees[0]:
            result[r] = fees[1]
            continue
        result[r] -= fees[0]
        if result[r] % fees[2] != 0:
            result[r] //= fees[2]
            result[r] += 1
        else:
            result[r] /= fees[2]
        result[r] *= fees[3]
        result[r] += fees[1]
        result[r] = int(result[r])


    return list(result.values())


# 기본시간, 기본요금, 단위시간, 단위요금
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))