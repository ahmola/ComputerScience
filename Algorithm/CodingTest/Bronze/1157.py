word = input("").lower()

# 알파벳은 26개, a는 97부터 시작, A는 65부터
check = [0] * 26

for w in word :
    i = ord(w) - 97
    if 0 <= i <= 25 :
        check[i] += 1

max_index = check.index(max(check))
isnot_dup = True

for i in range(26) :
    if i != max_index and check[i] == check[max_index] :
        isnot_dup = False
        print("?")
        break

if isnot_dup :
    print(chr(max_index + 65))