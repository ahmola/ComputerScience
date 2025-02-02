t = int(input(""))
# 학생의 반 기록
student = []
# 학생별 같은 반이었는지 체크 [[0]*t]*t 방식으로 초기화하지 말자 처음만든 리스트를 반복하기만 해서 다른 리스트들이 맨 위 리스트를 참조해서 변경하면 문제 발생함(2시간 낭비함;;)
result = [[0]* t for _ in range(t)]

for _ in range(t) :
    student.append(list(map(int, input().split())))

# 각 학년(열)마다 검사하는데 result에 얼마나 많은 학생(행)이랑 같은 반이 되었는지 기록
for i in range(t) :
    for j in range(t) :
        for k in range(5) :
            if i != j and student[i][k] == student[j][k] :
                result[i][j] = 1
                
count = [0] * t
for i in range(t) :
    for j in range(t) :
        if result[i][j] == 1 :
            count[i] += 1

print(count.index(max(count))+1)