with open('input13.txt', 'r') as file:
    ignore = file.readline()
    all_buses = file.readline().strip().split(",")

buses = []
for bus in all_buses:
    if bus == 'x':
        buses.append(0)
    else:
        buses.append(int(bus))

modulus = 1
for bus in buses:
    if bus != 0:
        modulus *= bus

time = 0
for bus in buses:
    if bus != 0:
        time += -buses.index(bus) * (modulus // bus) * pow(modulus // bus, -1, bus)

print(time % modulus)
