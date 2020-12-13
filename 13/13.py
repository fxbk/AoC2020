import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')
arrival = int(input[0])
busses = input[1].split(',')
busses = [int(bus) for bus in busses if bus != 'x']
print(busses)

next_departures = []
for bus in busses:
    next_departure_per_bus = bus
    while next_departure_per_bus <= arrival:
        next_departure_per_bus += bus
    next_departures.append(next_departure_per_bus)

print(f'Solutions part 1: {busses[np.argmin(next_departures)] * (min(next_departures) - arrival)}')
