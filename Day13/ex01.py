with open('input13.txt', 'r') as file:
    time = int(file.readline().strip())
    all_buses = file.readline().strip().split(",")

running_buses = list(filter(('x').__ne__, all_buses))
buses = [int(i) for i in running_buses]
max_time = time + int(max(buses))

schedules = []

for bus in buses:
    schedule = []
    for arrival in range(0, max_time, bus):
        if arrival > time:
            schedule.append(arrival)
            schedule.append(bus)
            break
    schedules.append(schedule)

first_arrivals = []
for n in schedules:
    first_arrivals.append(n)

arrival_time = min(first_arrivals)[0]
bus = min(first_arrivals)[1]
print("Arrival time:", arrival_time, "After:", arrival_time - time, "bus:", bus, "Answer:", bus * (arrival_time - time))
