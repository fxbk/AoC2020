def to_decimal(list, zero, one):
    binarys = []
    for elem in list:
        bin = ''
        for c in elem:
            if c == zero:
                bin += ('0')
            elif c == one:
                bin += ('1')
        binarys.append(int(bin, 2))
    return binarys


file = open('input.txt', 'r')
input = file.read().split('\n')
rows = [x[:7] for x in input]
rows_binary = to_decimal(rows, 'F', 'B')

seats = [x[7:] for x in input]
seats_binary = to_decimal(seats, 'L', 'R')

seat_id = sorted([row*8 + seat for row, seat in list(zip(rows_binary, seats_binary))])
print(seat_id[-1])

print([item for item in list(range(seat_id[0], seat_id[-1])) if item not in seat_id])


