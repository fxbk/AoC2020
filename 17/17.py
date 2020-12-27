import copy
import itertools

file = open('input2.txt', 'r')
input = file.read()
input = input.split('\n')

active = []
for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c == '#':
            active.append((x, y, 0))


input = [[list('...') for i in range(4)], [list(line) for line in input] + [list('...')], [list('...') for i in range(4)]]


def get_number_of_active_neighbors(system, x, y, z):
    number_of_active_neighbors = 0
    neighbors = list(itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    del neighbors[neighbors.index((0, 0, 0))]
    for neighbor in neighbors:
        x_idx = x + neighbor[0]
        y_idx = y + neighbor[1]
        z_idx = z + neighbor[2]
        if 0 <= x_idx < len(system[0][0]) and 0 <= y_idx < len(system[0]) and 0 <= z_idx < len(system):
            if system[z_idx][y_idx][x_idx] == '#':
                number_of_active_neighbors += 1
    return number_of_active_neighbors


out = copy.deepcopy(input)
for z, dim in enumerate(input):
    for y, row in enumerate(dim):
        for x, elem in enumerate(row):
            numb_neigbbors = get_number_of_active_neighbors(input, x, y, z)
            if elem == '#' and numb_neigbbors not in [2, 3]:
                out[z][y][x] = '.'
            elif elem == '.' and numb_neigbbors == 3:
                out[z][y][x] = '#'

print(out[0])
print(out[1])
print(out[2])