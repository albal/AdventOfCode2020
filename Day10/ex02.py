data = []

with open('input10.txt', 'r') as file:
    for line in file:
        data.append(int(line.strip()))

data.append(0)                          # Add the socket
data.append(max(data) + 3)              # Add the last adapter
data.sort(reverse=True)                 # Descending sort

perms = {i: 1 for i in data}            # there is at least one permutation, populate key/value for each adapter
for k in data:                          # for each key in path
    if k != max(data):                  # check we are not last
        t = 0
        for n in 1, 2, 3:               # for each valid step
            if k + n in perms:          # we have a fit
                t = t + perms[k + n]    # top up total
        perms[k] = t                    # store total

print("Permutations:", perms[0])        # last element has all permutations
