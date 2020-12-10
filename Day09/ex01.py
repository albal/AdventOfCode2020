data = []

with open('input09.txt', 'r') as file:
    for line in file:
        data.append(int(line.strip()))

print(data)

count = 0
preamble = 25

for n in range(preamble, len(data)):
    vals = data[n-preamble:n]
    target = data[n]
    print("Target", target, "from", vals, end='')
    match = False
    for i in vals:
        for j in vals:
            if i + j == target:
                match = True
    if match:
        print(" ***** Match *****")
    else:
        print(" XXX No match XXXX")
        exit(0)
