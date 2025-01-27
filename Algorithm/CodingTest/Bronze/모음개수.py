str = ""
answer = []

while True :
    str = input("")
    if str == "#" :
        break
    count = 0

    for char in str :
        if char in "aeiouAEIOU":
            count += 1

    answer.append(count)

for i in range(len(answer)) :
    print(answer[i])