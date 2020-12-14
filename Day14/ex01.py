import re

with open('input14.txt', 'r') as file:
    data = file.read().strip().split('\n')

addresses = {}
mask = ""

for line in data:
    if line.startswith("mask"):
        mask = line.split('=')[1].strip()
    if line.startswith("mem"):
        location, value = re.findall(r"mem\[(\d+)\] = (\d+)", line)[0]
        bin_value = bin(int(value))
        val = "0" * (len(mask) - len(bin_value) + 2) + bin_value[2:]
        new_val = ""
        for count, bit in enumerate(val):
            if mask[count] == '1':
                bit = "1"
            if mask[count] == '0':
                bit = "0"
            new_val += bit
        addresses[location] = int(new_val, 2)

print(sum(addresses.values()))

