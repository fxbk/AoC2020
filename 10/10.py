file = open('input.txt', 'r')
input = file.read().split('\n')
input = [int(x) for x in input]

input = sorted(input)
print(input)
counter_diff_one = 1
counter_diff_three = 1
for idx, x in enumerate(input[:len(input)-1]):
    if input[idx + 1] - x == 1:
        counter_diff_one += 1
    elif input[idx + 1] - x == 3:
        counter_diff_three += 1
print(f'Solutions to part 1: {counter_diff_one * counter_diff_three}')

# Part 2