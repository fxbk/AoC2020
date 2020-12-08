file = open('input.txt', 'r')
input = file.read().split('\n')
input = [[x[0], int(x[1])] for x in [x.split(' ') for x in input]]
accumulator = 0
visited = []
current_instructio_idx = 0

while True:
    if current_instructio_idx in visited:
        break
    visited.append(current_instructio_idx)
    if input[current_instructio_idx][0] == 'acc':
        accumulator += input[current_instructio_idx][1]
        current_instructio_idx += 1
    elif input[current_instructio_idx][0] == 'jmp':
        current_instructio_idx += input[current_instructio_idx][1]
    else:
        current_instructio_idx += 1

print(f'Solution Part 1: {accumulator}')

# Part 2
def run_program(input):
    current_instructio_idx = 0
    visited = []
    accumulator = 0
    while current_instructio_idx < len(input):
        if current_instructio_idx in visited:
            return False, accumulator
        visited.append(current_instructio_idx)
        if input[current_instructio_idx][0] == 'acc':
            accumulator += input[current_instructio_idx][1]
            current_instructio_idx += 1
        elif input[current_instructio_idx][0] == 'jmp':
            current_instructio_idx += input[current_instructio_idx][1]
        else:
            current_instructio_idx += 1
    return True, accumulator
import copy
jmp = [idx for idx, x in enumerate(input) if x[0] == 'jmp']
nop = [idx for idx, x in enumerate(input) if x[0] == 'nop']
replaced = []
for idx in jmp:
    one_changed_input = copy.deepcopy(input)
    one_changed_input[idx][0] = 'nop'
    terminate, accumulator = run_program(one_changed_input)
    if terminate:
        print(f'Solution to Part 2: {accumulator}')
        break
for idx in nop:
    one_changed_input = input
    one_changed_input[idx][0] = 'jmp'
    terminate, accumulator = run_program(one_changed_input)
    if terminate:
        print(f'Solution to Part 2: {accumulator}')
        break
