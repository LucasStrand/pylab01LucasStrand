with open("score2.txt", "r") as f:
    d = {}
    for line in f.readlines():
        line = line.split()
        firstName = line[2]
        lastName = line[3]
        fullName = firstName + lastName
        score = line[4]
        #d[fullName] = score
        d[fullName] = d.get(fullName, 0) + int(score)


#find all values, then take the max one
all_values = d.values()
max_value = max(all_values)

listOfKeys = list()
#iterate through all the items in dcitionary to find the keys with the max value
for fullName, score in d.items():
    if score == max_value:
        listOfKeys.append(fullName)

print("Key(s) with the max value in the dictionary: ", listOfKeys, "The value: ", max_value)