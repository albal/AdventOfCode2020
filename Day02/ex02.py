with open('input02.txt', 'r') as file:
    data = file.readlines()

valid = 0
valid2 = 0
for line in data:
    entry = line.strip('\n')
    print(entry)
    items = entry.split(' ')
    pos1 = int(items[0].split('-')[0])
    pos2 = int(items[0].split('-')[1])
    char = items[1][0]
    password = items[2]
    char1 = password[pos1-1]
    char2 = password[pos2-1]

    if (char1 != char and char2 == char) or (char1 == char and char2 != char):
        valid += 1

    bool1 = bool(char1 == char)
    bool2 = bool(char2 == char)

    if bool1 != bool2:
        valid2 += 1


    print("Comparing",char,"with", char1, "and", char2, "in", password,"(", char1 != char2,")")


print(valid)
print(valid2)
