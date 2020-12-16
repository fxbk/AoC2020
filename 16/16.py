file = open('input2.txt', 'r')
input = file.read()
input = input.split('\n\n')

fields_values = input[0].split('\n')
fields = [x.split(': ')[0] for x in fields_values]
ranges = [(x[0].split('-'), x[1].split('-')) for x in [x.split(': ')[1].split(' or ') for x in fields_values]]
fields_values_dict = dict(zip(fields, ranges))

my_ticket = input[1].split('\n')[1].split(',')

nearby_tickets = input[2].split('\n')
nearby_tickets = [x.split(',') for x in nearby_tickets[1:]]


def check_value(value, fields_values_dict):
    out = []
    for ranges in fields_values_dict.values():
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


def combine_checks(list_of_lists):
    out = []
    for list in list_of_lists:
        tmp = []
        for idx in np.arange(len(list))[::2]:
            tmp.append(list[idx] or list[idx+1])
        out.append(tmp)
    return out


for field, ranges in fields_values_dict.items():
    valid_list = []
    for ticket in cleaned_tickets:
        for value in ticket:
            value = int(value)
            valid_list.append(check_value(value, fields_values_dict))
    valid_list = combine_checks(valid_list)
    valid_matrix = np.matrix(valid_list)
    fields_in_right_order.append(fields[np.argmax(np.sum(valid_matrix, axis=0))])

print(fields_in_right_order)
