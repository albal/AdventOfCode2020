test_data = [0, 3, 6]               # 2020th 436
test_data = [13, 16, 0, 12, 15, 1]  # 2020th ?

count, spoken, last = 0, 0, {}

for i in test_data:
    count += 1
    last[i] = count

spoken = i

#while count < 2020:
while count < 30000000:
    memory = last.get(spoken)
    last[spoken] = count
    if memory:
        spoken = count - memory
    else:
        spoken = 0
    count += 1

print(spoken)
