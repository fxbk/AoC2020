import copy

file = open('input.txt', 'r')
input = file.read().split()
data = []
for idx, s in enumerate(input):
    chars = []
    for c in s:
        chars.append(c)
    data.append(chars)
print(data)


def get_adjoints(row, column, data):
    if row == 0 and column == 0:
        adjent = [(0, 1), (1, 0), (1, 1)]
    elif row == 0 and column < len(data[0])-1:
        adjent = [(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    elif row == 0 and column == len(data[0])-1:
        adjent = [(0, -1), (1, -1), (1, 0)]
    elif row == len(data)-1 and column == 0:
        adjent = [(-1, 0), (-1, 1), (0, 1)]
    elif row == len(data)-1 and column < len(data[0])-1:
        adjent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1)]
    elif row == len(data)-1 and column == len(data[0])-1:
        adjent = [(-1, -1), (-1, 0), (0, -1)]
    elif row < len(data)-1 and column == 0:
        adjent = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1)]
    elif row < len(data)-1 and column == len(data[0])-1:
        adjent = [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0)]
    else:
        # row < len(data)-1 and column < len(data[0])-1:
        adjent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    empty = 8 - len(adjent)
    for y, x in adjent:
        if data[row + y][column + x] == 'L' or data[row + y][column + x] == '.':
            empty += 1

    return empty


def simulate_seating(data):
    while True:
        out = copy.deepcopy(data)
        for row in range(len(data)):
            for column in range(len(data[0])):
                if out[row][column] == '.':
                    continue
                empty = get_adjoints(row, column, data)
                if empty == 8:
                    out[row][column] = '#'
                if 8 - empty >= 4:
                    out[row][column] = 'L'
        if out == data:
            break
        else:
            data = out
    return out


final_seating = simulate_seating(data)
occupied_seats = 0
for row in range(len(final_seating)):
    for column in range(len(final_seating[0])):
        if final_seating[row][column] == '#':
            occupied_seats += 1

print(f'Solution part 1: {occupied_seats}')


