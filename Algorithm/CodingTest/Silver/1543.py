doc = input("")
char = input("")
count = 0

while len(doc) >= len(char) and len(doc) != 0:
    index = doc.find(char)
    if index != -1 :
        count += 1
        doc = doc[index+len(char):]
    else :
        break
print(count)