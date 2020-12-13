import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')
arrival = int(input[0])
busses = input[1].split(',')
busses_small = [int(bus) for bus in busses if bus != 'x']
print(busses)

next_departures = []
for bus in busses_small:
    next_departure_per_bus = bus
    while next_departure_per_bus <= arrival:
        next_departure_per_bus += bus
    next_departures.append(next_departure_per_bus)

print(f'Solutions part 1: {busses_small[np.argmin(next_departures)] * (min(next_departures) - arrival)}')

# Part 2
busses = [x if x == 'x' else int(x) for x in busses]
max_value = max(busses_small)
max_value_idx = busses.index(max_value)
t = (100000000000000 + (max_value - (100000000000000 % max_value))) + (max_value - max_value_idx)

while True:
    counter = 0
    for idx, x in enumerate(busses):
        if x == 'x':
            counter += 1
            continue
        elif (t + idx) % x == 0:
            counter += 1
        else:
            break
    if counter == len(busses):
        break
    else:
        t += max_value

print(t)

'''
55
114
173
232
291
350
409
468
527
'''

# First solution, but it will takes for ever (9.921098947525024 seconds per 1 million runs)
'''
def check_sequence(plan, goal):
    counter = 0
    start_idx = len(plan) - len(goal)
    for idx, x in enumerate(goal):
        if x == 'x':
            counter += 1
        else:
            if int(x) in plan[start_idx + idx]:
                counter += 1
    return counter == len(goal)
plan = []
busses_array = np.array(busses_small)
t = 0
import time
start_time = time.time()
while True:
    if t % 1000000 == 0:
        print(t)
        print(time.time() - start_time)
    if t > len(busses):
        plan = plan[len(plan)-len(busses):]
        if check_sequence(plan, busses):
            break
    tmp = []
    for bus in busses_small:
        if t % bus == 0:
            tmp.append(bus)
    plan.append(tmp)
    t += 1

print(t-len(busses))
'''
