with open('input05.txt', 'r') as file:
    data = file.read().splitlines()


def decode(code):
    binary = [1, 2, 4, 8, 16, 32, 64, 128]
    index = 0
    val = 0
    for char in reversed(code):
        if char == 'B' or char == 'R':
            val += binary[index]
        index += 1
    return val


seats = [i for i in range(89, 889)]

for boardingpass in data:
    coded_row = boardingpass[:7]
    coded_col = boardingpass[7:]

    row = decode(coded_row)
    col = decode(coded_col)

    seat_id = (row * 8) + col
    seats.remove(seat_id)

print("Seat remaining:", seats[0])

