import re
import sys
sys.setrecursionlimit(10000)

file = open('input.txt', 'r')
input = file.read().split('\n')
rules_dict = {x[0]: re.split(' bags, | bag, ', x[1]) for x in [x.split(' bags contain ') for x in input]}

for key, value in rules_dict.items():
    for idx, val in enumerate(value):
        for c in [str(i) + ' ' for i in range(10)] + [' bags.', ' bag.']:
            value[idx] = value[idx].replace(c, '')
    rules_dict[key] = value

rules_dict['no other'] = []

def recursive(dict, values):
    if len(values) == 0:
        return []
    else:
        return [values[0]] + recursive(dict, list(set(values[1:] + dict[values[0]])))

counter = 0
for key in rules_dict.keys():
    print(recursive(rules_dict, rules_dict[key]))
    if 'shiny gold' in recursive(rules_dict, rules_dict[key]):
        counter += 1

print(counter)
# def recursive(dict, key):
#     if 'shiny gold' in dict[key]:
#         return True
#     else:
#         return False or recursive(dict, key, dict[key])
#
# counter = 0
# for key in rules_dict.keys():
#     if key == 'shiny gold':
#         counter += 1
#         continue
#     if recursive(rules_dict, key):
#         counter += 1
#
# print(counter)
