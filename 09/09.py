file = open('input.txt', 'r')
input = file.read().split('\n')
input = [int(x) for x in input]


def get_possible_sum(data, preamble_length, idx):
    preamble = data[idx - preamble_length: idx]
    out = []
    for idx, x in enumerate(preamble):
        for idy, y in enumerate(preamble):
            if idx == idy:
                continue
            out.append(x + y)
    return out


def check_input(data, preamble_length):
    for idx, x in enumerate(data[preamble_length+1:]):
        idx += preamble_length + 1
        if x not in get_possible_sum(data, preamble_length, idx):
            return x
            break

invalid_numer = check_input(input, 25)
print(f'Solution part 1: {invalid_numer}')

for idx, x in enumerate(input):
    summands = []
    sum = 0
    i = 0
    while sum < invalid_numer:
        sum += input[idx + i]
        summands.append(input[idx + i])
        i += 1
    if sum == invalid_numer:
        print(f'Solution part 2: {min(summands) + max(summands)}')
        break
