file = open('input.txt', 'r')
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


sum = 0
for calculation in input:
    new_value, _ = calculate_values(calculation)
    print(new_value)
    sum += new_value

print(f'Solution part 1: {sum}')
