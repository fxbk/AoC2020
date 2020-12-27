import copy
import itertools
from tqdm import tqdm


file = open('input.txt', 'r')
input = file.read()
input = input.split('\n')

active = []
for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c == '#':
            active.append((x, y, 0))


def get_number_of_active_neighbors(active_list, x, y, z):
    number_of_active_neighbors = 0
    neighbors = list(itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    del neighbors[neighbors.index((0, 0, 0))]
    for neighbor in neighbors:
        x_idx = x + neighbor[0]
        y_idx = y + neighbor[1]
        z_idx = z + neighbor[2]
        if (x_idx, y_idx, z_idx) in active_list:
            number_of_active_neighbors += 1
    return number_of_active_neighbors


x_max = len(input[0])
y_max = len(input)
z_max = 0

for cycle in range(1, 7):
    out = copy.deepcopy(active)
    for z in range(-cycle, cycle + 1):
        for y in range(-cycle, y_max + cycle + 1):
            for x in range(-cycle, x_max + cycle + 1):
                numb_neigbbors = get_number_of_active_neighbors(active, x, y, z)
                if (x, y, z) in active and numb_neigbbors not in [2, 3]:
                    del out[out.index((x, y, z))]
                elif (x, y, z) not in active and numb_neigbbors == 3:
                    out.append((x, y, z))
    active = out

print(f'Solution part 1: {len(out)}')

# Part 2
active = []
for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c == '#':
            active.append((x, y, 0, 0))


def get_number_of_active_neighbors_part2(active_list, x, y, z, w):
    number_of_active_neighbors = 0
    neighbors = list(itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    del neighbors[neighbors.index((0, 0, 0, 0))]
    for neighbor in neighbors:
        x_idx = x + neighbor[0]
        y_idx = y + neighbor[1]
        z_idx = z + neighbor[2]
        w_idx = w + neighbor[3]
        if (x_idx, y_idx, z_idx, w_idx) in active_list:
            number_of_active_neighbors += 1
    return number_of_active_neighbors


x_max = len(input[0])
y_max = len(input)
# TODO Adjust range in order to cure the curse of dimensionality i.e. delete row, column if no point active there
for cycle in tqdm(range(1, 7), 'Cycles: '):
    out = copy.deepcopy(active)
    for w in tqdm(range(-cycle, cycle + 1), 'W Dimension'):
        for z in range(-cycle, cycle + 1):
            for y in range(-cycle, y_max + cycle + 1):
                for x in range(-cycle, x_max + cycle + 1):
                    numb_neigbbors = get_number_of_active_neighbors_part2(active, x, y, z, w)
                    if (x, y, z, w) in active and numb_neigbbors not in [2, 3]:
                        del out[out.index((x, y, z, w))]
                    elif (x, y, z, w) not in active and numb_neigbbors == 3:
                        out.append((x, y, z, w))
    active = out

print(f'Solution part 2: {len(out)}')
