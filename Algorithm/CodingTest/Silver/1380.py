n = 1
result = []

while n != 0 :
    student = []
    earing = {}
    # 학생 입력
    n = int(input("")) 
    for _ in range(n) :
        student.append(input(""))
    
    # 2n - 1
    for i in range(2*n-1) :
        number, char = map(str, input().split())
        # 있는데 문자가 다르면
        if number in earing and earing[number] != char:
            earing.pop(number)
        # 없다면 추가
        else :
            earing[number] = char
    
    # 돌려받지 못한 학생 저장
    for i in earing :
        result.append(student[int(i)-1])

for r in result :
    print(f"{result.index(r)+1} {r}")
    

        
    
    