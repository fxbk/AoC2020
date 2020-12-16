file = open('input.txt', 'r')
input = file.read()
input = input.split('\n\n')

fields_values = input[0].split('\n')
fields = [x.split(': ')[0] for x in fields_values]
ranges = [(x[0].split('-'), x[1].split('-')) for x in [x.split(': ')[1].split(' or ') for x in fields_values]]
fields_values_dict = dict(zip(fields, ranges))
print(fields_values_dict)

my_ticket = input[1].split('\n')[1].split(',')
print(my_ticket)

nearby_tickets = input[2].split('\n')
nearby_tickets = [x.split(',') for x in nearby_tickets[1:]]
print(nearby_tickets)


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

print(error)
