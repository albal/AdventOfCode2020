with open('input02.txt', 'r') as file:
    data = file.readlines()

valid = 0

for line in data:
    entry = line.strip('\n')
    print(entry)
    items = entry.split(' ')
    range_start = int(items[0].split('-')[0])
    range_end = int(items[0].split('-')[1])
    char = items[1][0]
    password = items[2]
    count = password.count(char)
    print("From", range_start, "to", range_end, "looking for", char, "in", password, "has", count, "occurences")
    if range_start <= count <= range_end:
        valid += 1

print(valid)
