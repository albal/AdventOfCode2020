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

max_id = 0
seats = 0

for boardingpass in data:
    seats += 1
    coded_row = boardingpass[:7]
    coded_col = boardingpass[7:]

    row = decode(coded_row)
    col = decode(coded_col)

    seat_id = (row * 8) + col
    if seat_id > max_id:
        max_id = seat_id

    print("Boarding pass is:", boardingpass, " with row:", row, " and col:", col, " and id:", seat_id, " Max ID:", max_id)

print("Processed", seats, "seats")


