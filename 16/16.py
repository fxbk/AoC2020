file = open('input.txt', 'r')
input = file.read()
input = input.split('\n\n')

fields_values = input[0].split('\n')
fields = [x.split(': ')[0] for x in fields_values]
ranges = [(x[0].split('-'), x[1].split('-')) for x in [x.split(': ')[1].split(' or ') for x in fields_values]]
fields_values_dict = dict(zip(fields, ranges))

my_ticket = input[1].split('\n')[1].split(',')

nearby_tickets = input[2].split('\n')
nearby_tickets = [x.split(',') for x in nearby_tickets[1:]]


def check_value(value, dict):
    out = []
    for ranges in dict.values():
        for range in ranges:
            if int(range[0]) <= value <= int(range[1]):
                out.append(True)
            else:
                out.append(False)
    return out


error = 0
for ticket in nearby_tickets:
    for value in ticket:
        value = int(value)
        if not any(check_value(value, fields_values_dict)):
            error += value

print(f'Solution part 1: {error}')

# Part 2
cleaned_tickets = []
for ticket in nearby_tickets:
    valid = True
    for value in ticket:
        value = int(value)
        if not any(check_value(value, fields_values_dict)):
            valid = False
    if valid:
        cleaned_tickets.append(ticket)

import numpy as np
fields_in_right_order = []


def check_value_part2(value, dict):
    out = []
    for ranges in dict.values():
        valid = False
        for range in ranges:
            if int(range[0]) <= value <= int(range[1]):
                valid = True
        out.append(valid)
    return out

sums = []
for idx in range(len(cleaned_tickets[0])):
    tmp = []
    for ticket in cleaned_tickets:
        tmp.append(check_value_part2(int(ticket[idx]), fields_values_dict))
    sums.append(np.sum(np.matrix(tmp), axis=0))

indices_in_order = [i[0] for i in sorted(enumerate(sums), key=lambda x: np.sum(x[1]))]
fields_in_right_order = [fields[i] for i in indices_in_order]
print(fields_in_right_order)
results = []
result = 1
for idx, cls in enumerate(fields_in_right_order):
    if 'departure' in cls:
        results.append(int(my_ticket[idx]))
        result *= int(my_ticket[idx])
print(result)


'''
indices = []
while len(fields_in_right_order) < len(fields):
    print(fields_in_right_order)
    for idx2, sum in enumerate(sums):
        if idx2 in indices:
            continue
        # x = [x for i, x in enumerate(sum.tolist()[0]) if i not in indices]
        x = sum.tolist()[0]
        idxs = [i for i, value in enumerate(x) if value == 3]
        if len(set(idxs) - set(indices)) == 1+len(fields_in_right_order):
            fields_in_right_order.append(fields[idx2])
            indices.append(idx2)
            break
            
sums.sort(key=lambda x: np.sum(x))

indices = []
for sum in sums:
    # x = [x for i, x in enumerate(sum.tolist()[0]) if i not in indices]
    x = sum.tolist()[0]
    idxs = [i for i, value in enumerate(x) if value == 190]
    assert(len(set(idxs) - set(indices)) == 1)
    idx = (set(idxs) - set(indices)).pop()
    fields_in_right_order.append(fields[idx])
    indices.append(idx)
    # indices_left = [i for i in range(20) if i not in indices]
'''
