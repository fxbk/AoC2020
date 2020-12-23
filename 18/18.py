file = open('input2.txt', 'r')
input = file.read()
input = input.split('\n')
print(input)


def calculate_values(calculation):
    if calculation[0] == '(':
        value, new_idx = calculate_values(calculation[1:])
        idx = new_idx
    else:
        value = int(calculation[0])
        idx = 0
    operator = ''
    while idx < len(calculation[1:]):
        idx += 1
        c = calculation[idx]
        if c == ' ':
            continue
        elif c == ')':
            return value, idx+1
        elif c in ['*', '+']:
            operator = c
        elif c == '(':
            if operator == '+':
                new_value, new_idx = calculate_values(calculation[idx+1:])
                value += new_value
                idx += new_idx
            elif operator == '*':
                new_value, new_idx = calculate_values(calculation[idx+1:])
                value *= new_value
                idx += new_idx
        else:
            if operator == '+':
                value += int(c)
            elif operator == '*':
                value *= int(c)
    return value, idx


result = 0
for calculation in input:
    new_value, _ = calculate_values(calculation)
    print(new_value)
    result += new_value

print(f'Solution part 1: {result}')

# Part 2

def calculate_values_advanced(calculation):
    total_additions = sum([1 for c in calculation if c == '+'])
    executed_additions = 0
    total_multiplications = sum([1 for c in calculation if c == '*'])
    executed_multiplications = 0
    idx = 0
    result = 1
    calculation = list(calculation)
    while executed_additions < total_additions:
        if calculation[idx] == '+':
            calculation[idx] = int(calculation[idx-2]) + int(calculation[idx+2])
            del calculation[idx + 1]
            del calculation[idx + 1]
            del calculation[idx-1]
            del calculation[idx-2]
            executed_additions += 1
            idx -= 3
        idx += 1
    idx = 0
    while executed_multiplications < total_multiplications:
        if calculation[idx] == '*':
            calculation[idx] = int(calculation[idx - 2]) * int(calculation[idx + 2])
            del calculation[idx + 1]
            del calculation[idx + 1]
            del calculation[idx - 1]
            del calculation[idx - 2]
            executed_multiplications += 1
            idx -= 3
        idx += 1
    return calculation[0]

result = 0
for calculation in input:
    new_value = calculate_values_advanced(calculation)
    print(new_value)
    result += new_value

print(f'Solution part 2: {result}')
