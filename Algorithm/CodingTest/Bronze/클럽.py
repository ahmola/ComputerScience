person = ""
people = []

while True :
    person = input("")
    if person == "# 0 0" :
        break
    
    name, age, weight = person.split()
    if(int(age) > 17 or int(weight) >= 80) :
        people.append(name + " Senior")
    else :
        people.append(name + " Junior")

for i in range(len(people)) :
    print(people[i])