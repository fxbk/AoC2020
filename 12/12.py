import numpy as np


file = open('input.txt', 'r')
input = file.read().split('\n')
actions = [(x[0], int(x[1:])) for x in input]

print(input)

direction = 'E'
x = 0
y = 0
left_order = ['N', 'W', 'S', 'E']

for action in actions:
    # Forward
    if action[0] == 'F':
        if direction == 'E':
            x += action[1]
        elif direction == 'W':
            x -= action[1]
        elif direction == 'N':
            y += action[1]
        elif direction == 'S':
            y -= action[1]
    elif action[0] == 'E':
        x += action[1]
    elif action[0] == 'W':
        x -= action[1]
    elif action[0] == 'N':
        y += action[1]
    elif action[0] == 'S':
        y -= action[1]

    elif action[0] == 'L':
        idx = left_order.index(direction)
        idx += int(action[1] / 90)
        direction = left_order[idx % len(left_order)]

    elif action[0] == 'R':
        idx = left_order.index(direction)
        idx -= int(action[1] / 90)
        direction = left_order[idx % len(left_order)]

print(x, y)
print(f'Solutions part 1: {np.linalg.norm(np.array([x,y]), ord=1)}')

