file = open('input.txt', 'r')
input = file.read().split('\n')
right_bound = len(input[0])
trees = 0
x = 0
y = 0

while y < len(input):
    if input[y][x % right_bound] == '#':
        trees += 1
    y += 1
    x += 3

print(trees)

patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] # Right, down
trees_multi = 1
for right, down in patterns:
    trees = 0
    x = 0
    y = 0
    while y < len(input):
        if input[y][x % right_bound] == '#':
            trees += 1
        y += down
        x += right
    print(trees)
    trees_multi *= trees

print(trees_multi)