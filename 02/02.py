file = open('input.txt', 'r')
input = file.read().split('\n')
policy_list = [(int(x[0].split('-')[0]), int(x[0].split('-')[1]), x[1][0], x[2]) for x in [x.split() for x in input]]
correct = 0

for low, high, char, pswd in policy_list:
    counter = 0
    for c in pswd:
        if c == char:
            counter += 1
    if low <= counter <= high:
        correct += 1
print(correct)

# Part 2
correct = 0
for low, high, char, pswd in policy_list:
    if pswd[low - 1] == char:
        if pswd[high - 1] != char:
            correct += 1
    if pswd[high - 1] == char:
        if pswd[low - 1] != char:
            correct += 1

print(correct)
