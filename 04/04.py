import re
file = open('input.txt', 'r')
input = file.read().split('\n\n')
# input = [x[0].split('\n') for x in [x.split(' ') for x in input]]

passport = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
counter = 0
for batch in input:
    batch = re.split(' |\n', batch)
    if len(batch) == 8:
        counter += 1
    elif len(batch) == 7:
        elems = []
        for x in batch:
            elems.append(x[:3])
        if set(elems) == passport:
            counter += 1
print(counter)

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''
def check(keys, values):
    for idx, key in enumerate(keys):
        if not _check_helper(key, values, idx):
            return False
    return True


def _check_helper(key, values, idx):
    if key == 'byr':
        if len(values[idx]) == 4 and 1920 <= int(values[idx]) <= 2002:
            return True
    if key == 'iyr':
        if len(values[idx]) == 4 and 2010 <= int(values[idx]) <= 2020:
            return True
    if key == 'eyr':
        if len(values[idx]) == 4 and 2020 <= int(values[idx]) <= 2030:
            return True
    if key == 'hgt':
        if values[idx][len(values[idx]) - 2:] == 'cm' and len(values[idx]) == 5 and \
                150 <= int(values[idx][:3]) <= 193:
            return True
        if values[idx][len(values[idx]) - 2:] == 'in' and len(values[idx]) == 4 and \
                59 <= int(values[idx][:2]) <= 76:
            return True
    if key == 'hcl':
        if values[idx][0] == '#' and len(values[idx]) == 7:
            patttern = re.compile('[0-9a-f]')
            for c in values[idx][1:]:
                if patttern.match(c) is None:
                    return False
            return True
    if key == 'ecl':
        if values[idx] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    if key == 'pid':
        if len(values[idx]) == 9:
            patttern = re.compile('[0-9]')
            for c in values[idx][1:]:
                if patttern.match(c) is None:
                    return False
            return True
    if key == 'cid':
        return True
    return False

counter = 0
for batch in input:
    batch = re.split(' |\n', batch)
    keys = []
    values = []
    for x in batch:
        keys.append(x[:3])
        values.append(x[4:])
    if len(keys) == 8:
        if check(keys, values):
            counter += 1
    elif len(keys) == 7:
        if set(keys) == passport:
            if check(keys, values):
                counter += 1
print(counter)