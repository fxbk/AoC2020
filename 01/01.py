def part1():
    file = open('input.txt', 'r')
    input = file.read().split('\n')
    input = [int(x) for x in input]

    for idx1, x in enumerate(input):
        for idx2, y in enumerate(input):
            if x + y == 2020:
                print(x, y)
                print(x*y)


def part2():
    file = open('input2.txt', 'r')
    input = file.read().split('\n')
    input = [int(x) for x in input]
    for x in input:
        for y in input:
            for z in input:
                if x + y + z == 2020:
                    print(x, y, z)
                    print(x * y * z)