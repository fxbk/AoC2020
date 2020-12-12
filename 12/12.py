import numpy as np
import copy

file = open('input.txt', 'r')
input = file.read().split('\n')
actions = [(x[0], int(x[1:])) for x in input]

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

    # Move directly in the given direction
    elif action[0] == 'E':
        x += action[1]
    elif action[0] == 'W':
        x -= action[1]
    elif action[0] == 'N':
        y += action[1]
    elif action[0] == 'S':
        y -= action[1]

    # Change direction
    elif action[0] == 'L':
        idx = left_order.index(direction)
        idx += int(action[1] / 90)
        direction = left_order[idx % len(left_order)]
    elif action[0] == 'R':
        idx = left_order.index(direction)
        idx -= int(action[1] / 90)
        direction = left_order[idx % len(left_order)]

print(x, y)
print(f'Solutions part 1: {int(np.linalg.norm(np.array([x,y]), ord=1))}')

waypoint = np.array([10, 1])
ship = np.array([0, 0])

for action in actions:
    # Forward
    if action[0] == 'F':
        ship += action[1] * waypoint

    # Move waypoint directly in the given direction
    elif action[0] == 'E':
        waypoint += np.array([action[1], 0])
    elif action[0] == 'W':
        waypoint -= np.array([action[1], 0])
    elif action[0] == 'N':
        waypoint += np.array([0, action[1]])
    elif action[0] == 'S':
        waypoint -= np.array([0, action[1]])

    # Rotate waypoint
    elif action[0] == 'L':
        for i in range(int(action[1] / 90)):
            tmp = copy.copy(waypoint[0])
            waypoint[0] = - waypoint[1]
            waypoint[1] = tmp
    elif action[0] == 'R':
        for i in range(int(action[1] / 90)):
            tmp = copy.copy(waypoint[0])
            waypoint[0] = waypoint[1]
            waypoint[1] = - tmp

print(ship)
print(f'Solutions part 2: {int(np.linalg.norm(ship, ord=1))}')
