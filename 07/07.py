import re

file = open('input.txt', 'r')
input = file.read().split('\n')
rules_dict = {x[0]: re.split(' bags, | bag, ', x[1]) for x in [x.split(' bags contain ') for x in input]}

for key, value in rules_dict.items():
    for idx, val in enumerate(value):
        for c in [str(i) + ' ' for i in range(10)] + [' bags.', ' bag.']:
            value[idx] = value[idx].replace(c, '')
    rules_dict[key] = value

print(rules_dict)
def recursive(dict, key):
    if 'shiny gold' in dict[key]:
        return True
    for value in dict[key]:
        # print(value)
        if value != 'no other':
            recursive(dict, value)

counter = 0
for key in rules_dict.keys():
    if key == 'shiny gold':
        counter += 1
        continue
    if recursive(rules_dict, key):
        counter += 1

print(counter)
