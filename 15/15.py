file = open('input.txt', 'r')
input = file.read().split(',')
turns = input + ['0']
turns_minus_last = input

for i in range(len(turns), 30000000):
    if turns[i-1] in turns_minus_last:
        turns.append(str((i) - (len(turns_minus_last) - turns_minus_last[::-1].index(turns[i-1]))))
    else:
        turns.append('0')
    turns_minus_last.append(turns[i-1])

print(turns[-1])