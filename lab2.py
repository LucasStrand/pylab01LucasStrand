f = open("score2.txt", "r")
d = {}
for line in f.readlines():
    line = line.split()
    firstName = line[2]
    lastName = line[3]
    fullName = firstName + lastName
    score = line[4]
    d[fullName] = score
    for fullName, score in d.items():
        if score not in fullName:
            
        else:
            d[fullName] = d.get(fullName, 0) + int(score)
print(d)