import re
from enum import Enum


class Compass (Enum):
    North = 0
    East = 90
    South = 180
    West = 270


direction = Compass.East

Easting = 0
Northing = 0


def move_forward(units):
    global Easting, Northing
    if direction == Compass.East:
        Easting += units
    elif direction == Compass.West:
        Easting -= units
    elif direction == Compass.North:
        Northing += units
    elif direction == Compass.South:
        Northing -= units


def change_direction(direc, angle):
    global direction
    bearing = direction.value
    if direc == 'R':
        bearing += angle
    elif direc == 'L':
        bearing -= angle
    if bearing > 270:
        bearing -= 360
    if bearing < 0:
        bearing += 360
    direction = Compass(bearing)


with open('input12.txt', 'r') as file:
    data = file.read().strip().split('\n')

for line in data:
    inner_data = re.findall(r"^(\w)(\d+)$", line)
    command = inner_data[0][0]
    parameter = int(inner_data[0][1])
    if command == 'N':
        Northing += parameter
    elif command == "S":
        Northing -= parameter
    elif command == "E":
        Easting += parameter
    elif command == "W":
        Easting -= parameter
    elif command == "F":
        move_forward(parameter)
    else:  # command is L or R
        change_direction(command, parameter)

    print("East:", Easting, "North:", Northing, "Direction", direction)

print()
print("East:", Easting, "North:", Northing, "Manhattan:", abs(Northing) + abs(Easting))
