test_data = [0, 3, 6]               # 2020th 436
test_data = [13, 16, 0, 12, 15, 1]  # 2020th ?

count = 0
last = 0
for i in test_data:
    count += 1
    last = i

while count < 2020:
    if last in test_data:
        if test_data.count(last) == 1:
            last = 0
        else:
            rev = list(reversed(test_data))
            pos_last = rev.index(last)
            pos_prev = rev.index(last, pos_last + 1)
            last = pos_prev - pos_last
        test_data.append(last)
    else:
        test_data.append(0)
        last = 0
    count += 1

print(last)
