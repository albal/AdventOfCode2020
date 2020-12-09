with open('input03.txt', 'r') as file:
    data = file.readlines()
skip = True

step = 3

index = step
trees = 0
for line in data:
    if skip:
        skip = False
        continue
    pos = line[index].strip('\n')
    if pos == '#':
        trees += 1
    print(line.strip('\n'), " : Index is", index, " Trees hit:", trees)
    index += step
    if index >= len(line.strip('\n')):
        index = index - len(line.strip('\n'))
print("Trees hit:", trees)
