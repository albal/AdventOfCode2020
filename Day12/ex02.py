import re
from math import sin
from math import cos
from math import radians

Easting = 0
Northing = 0
waypointNorthing = 1
waypointEasting = 10


def move_forward(units):
    global Easting, Northing
    Northing += waypointNorthing * units
    Easting += waypointEasting * units


def change_direction(direc, angle):
    global waypointEasting, waypointNorthing
    bearing = 0.0
    if direc == 'L':
        bearing = radians(angle)
    else:
        bearing = radians(angle * -1)
    newWaypointEasting = round((waypointEasting * cos(bearing)) - waypointNorthing * sin(bearing))
    newWaypointNorthing = round((waypointEasting * sin(bearing)) + waypointNorthing * cos(bearing))
    waypointNorthing = newWaypointNorthing
    waypointEasting = newWaypointEasting


with open('input12.txt', 'r') as file:
    data = file.read().strip().split('\n')

for line in data:
    inner_data = re.findall(r"^(\w)(\d+)$", line)
    command = inner_data[0][0]
    parameter = int(inner_data[0][1])
    if command == 'N':
        waypointNorthing += parameter
    elif command == "S":
        waypointNorthing -= parameter
    elif command == "E":
        waypointEasting += parameter
    elif command == "W":
        waypointEasting -= parameter
    elif command == "F":
        move_forward(parameter)
    else:  # command is L or R
        change_direction(command, parameter)

    print("East:", Easting, "North:", Northing)

print()
print("East:", Easting, "North:", Northing, "Manhattan:", abs(Northing) + abs(Easting))
