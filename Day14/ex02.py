import re

with open('test14_2.txt', 'r') as file:
    data = file.read().strip().split('\n')

addresses = {}
locations = []
mask = ""


def split(input_mask):
    locs = []
    for c in range(len(input_mask)):
        if input_mask[c] == 'X':
            locs += split(input_mask[:c] + "1" + input_mask[c + 1:])
            locs += split(input_mask[:c] + "0" + input_mask[c + 1:])
            return locs
    return [input_mask]


for line in data:
    if line.startswith("mask"):
        mask = line.split('=')[1].strip()
    if line.startswith("mem"):
        location, value = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
        bin_value = bin(int(value))
        val = "0" * (len(mask) - len(bin_value) + 2) + bin_value[2:]
        new_mask = ""
        print("Mask:    ", mask)
        print("Location:", location)
        for count, bit in enumerate(val):
            if mask[count] == '1':
                bit = "1"
            if mask[count] == 'X':
                bit = "X"
            new_mask += bit

        print("New: ", new_mask)

        for m in split(new_mask):
            print(m)
            addresses[int(m, 2)] = int(value, 2)

print(sum(addresses.values()))

