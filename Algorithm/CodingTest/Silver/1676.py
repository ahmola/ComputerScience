def factorial(number) :
    if number == 1 or number == 0 :
        return 1
    else :
        return number*factorial(number-1)

n = int(input(""))
number = list(str(factorial(n)))

count = 0
for i in range(len(number)-1, -1, -1) :
    if number[i] != "0" :
        break
    count += 1
print(count)