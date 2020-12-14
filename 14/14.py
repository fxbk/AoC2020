import re
import itertools

file = open('input.txt', 'r')
input = file.read().split('\n')


def apply_bitmask(value, mask):
    value_binary = str(bin(value))[2:]
    for i in range(len(mask) - len(value_binary)):
        value_binary = '0' + value_binary
    out = ''
    for idx, c in enumerate(zip(mask, value_binary)):
        if c[0] == 'X':
            out = out + c[1]
        else:
            out = out + c[0]
    return int(out, 2)


mem = {}
for action in input:
    if action.startswith('mask'):
        mask = action[7:]
    else:
        match = re.search(r"\[([A-Za-z0-9_]+)\]", action).group(0)
        key = int(match[1:len(match)-1])
        value = int(action[6 + len(match):])
        mem[key] = apply_bitmask(value, mask)

print(f'Solution Part 1: {sum(mem.values())}')

# Part 2


def get_keys(value, mask):
    key_binary = str(bin(value))[2:]
    for i in range(len(mask) - len(key_binary)):
        key_binary = '0' + key_binary
    out = ''
    for idx, c in enumerate(zip(mask, key_binary)):
        if c[0] == 'X':
            out = out + c[0]
        elif c[0] == '1':
            out = out + c[0]
        elif c[0] == '0':
            out = out + c[1]
        else:
            out = out + c[0]
    return [int(x, 2) for x in get_options_floating(out)]


def get_options_floating(value):
    out = []
    x_indices = []
    for idx, c in enumerate(value):
        if c == 'X':
            x_indices.append(idx)
    fillings = list(itertools.product([0, 1], repeat=len(x_indices)))
    for fill in fillings:
        new_value = ''
        counter = 0
        for idx, x in enumerate(value):
            if idx in x_indices:
                new_value += str(fill[counter])
                counter += 1
            else:
                new_value += x
        out.append(new_value)
    return out


mem = {}
for action in input:
    if action.startswith('mask'):
        mask = action[7:]
    else:
        match = re.search(r"\[([A-Za-z0-9_]+)\]", action).group(0)
        keys = get_keys(int(match[1:len(match)-1]), mask)
        value = int(action[6 + len(match):])
        for key in keys:
            mem[key] = value

print(f'Solution Part 2: {sum(mem.values())}')