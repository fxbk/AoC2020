import copy
import itertools

file = open('input2.txt', 'r')
input = file.read()
input = input.split('\n')
input = [list(line) for line in input] + [list('...')]


def get_number_of_active_neighbors(system, x, y):
    number_of_active_neighbors = 0
    neighbors = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    del neighbors[neighbors.index((0, 0))]
    for neighbor in neighbors:
        x_idx = x + neighbor[0]
        y_idx = y + neighbor[1]
        if 0 <= x_idx < len(system[0]) and 0 <= y_idx < len(system):
            if system[y_idx][x_idx] == '#':
                number_of_active_neighbors += 1
    return number_of_active_neighbors


out = copy.deepcopy(input)
for y, row in enumerate(input):
    for x, elem in enumerate(row):
        numb_neigbbors = get_number_of_active_neighbors(input, x, y)
        if elem == '#' and numb_neigbbors not in [2, 3]:
            out[y][x] = '.'
        elif elem == '.' and numb_neigbbors == 3:
            out[y][x] = '#'

print(out)