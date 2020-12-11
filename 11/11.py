import copy

file = open('input2.txt', 'r')
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

# Part 2


def get_adjoints_directional(row, column, data):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    empty = 0
    for dir in directions:
        x = row
        y = column
        out = True
        while 0 <= y + dir[0] <= len(data)-1 and 0 <= x + dir[1] <= len(data[0])-1:
            y += dir[0]
            x += dir[1]
            if data[y][x] == 'L':
                empty += 1
                out = False
                break
            if data[y][x] == '#':
                out = False
                break
        if out:
            empty += 1
    return empty


def simulate_seating_part2(data):
    while True:
        out = copy.deepcopy(data)
        for row in range(len(data)):
            for column in range(len(data[0])):
                if out[row][column] == '.':
                    continue
                empty = get_adjoints_directional(row, column, data)
                if empty == 8:
                    out[row][column] = '#'
                if 8 - empty >= 5:
                    out[row][column] = 'L'
        print(out)
        if out == data:
            break
        else:
            data = out
    return out

final_seating2 = simulate_seating_part2(data)
occupied_seats_2 = 0
for row in range(len(final_seating2)):
    for column in range(len(final_seating2[0])):
        if final_seating2[row][column] == '#':
            occupied_seats_2 += 1

print(f'Solution part 1: {occupied_seats_2}')

