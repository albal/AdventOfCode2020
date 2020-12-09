with open('test03.txt', 'r') as file:
    data = file.readlines()

skip = True
skipAgain = True
step = 1

index = step
trees = 0
for line in data:
    if skip:
        skip = False
        continue
    if skipAgain:
        skipAgain = False
        continue
    pos = line[index].strip('\n')
    if pos == '#':
        trees += 1
    print(line.strip('\n'), " : Index is", index, " Trees hit:", trees)
    index += step
    if index >= len(line.strip('\n')):
        index = index - len(line.strip('\n'))
    skip = True
print("Trees hit:", trees)
