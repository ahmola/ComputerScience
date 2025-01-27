s = input("")

if s.count('"') and s.startswith('"') and s.endswith('"') :
    content = s[1:len(s)-1]
    if content:
        print(content)
    else:
        print("CE")
else :
    print("CE")