from operator import is_
from unittest import result


t = int(input(""))
result = 0

for _ in range(t) :
    word = input("")
    done_char = set()
    prev = ''
    is_group = True

    for w in word :
        if w != prev :
            if w in done_char :
                is_group = False
                break
            done_char.add(w)
        prev = w

    if is_group :
        result += 1

print(result)