import copy
from tqdm import tqdm

file = open('input.txt', 'r')
input = file.read().split(',')
turns = input + ['0']
turns_minus_last = copy.copy(input)

for i in range(len(turns), 2020):
    if turns[i-1] in turns_minus_last:
        turns.append(str((i) - (len(turns_minus_last) - turns_minus_last[::-1].index(turns[i-1]))))
    else:
        turns.append('0')
    turns_minus_last.append(turns[i-1])

print(f'Solutions part 1: {turns[-1]}')

# Part 2
turns = input + ['0']
turn_index = dict(zip(input, range(1, len(input)+1)))

for i in tqdm(range(len(turns), 30000000)):
    last_turn = turns[i-1]
    if last_turn in turn_index.keys():
        turns.append(str(i - turn_index[last_turn]))
    else:
        turns.append('0')
    turn_index[turns[i-1]] = i

print(f'Solutions part 2: {turns[-1]}')
