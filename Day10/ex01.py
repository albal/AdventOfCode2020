data = []

with open('input10.txt', 'r') as file:
    for line in file:
        data.append(int(line.strip()))

data.append(0)                      # Add the socket
data.append(max(data) + 3)          # Add the last adapter
data.sort()                         # Ascending sort

diff_1 = diff_3 = 0

for i, v in enumerate(data[:-1]):   # don't use last element as source
    if data[i + 1] == v + 1:
        diff_1 += 1
    elif data[i + 1] == v + 3:
        diff_3 += 1

print("Diff 1:", diff_1, "Diff 3:", diff_3, "Answer:", diff_1 * diff_3)
