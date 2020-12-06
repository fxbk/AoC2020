def get_list_of_characters(string):
    out = []
    string = string.replace('\n', '')
    for c in string:
        out.append(c)
    return out


file = open('input.txt', 'r')
input = file.read().split('\n\n')
list_of_union_answer = []
for x in input:
    list_of_union_answer.append(set(get_list_of_characters(x)))

print(f'Solution for part 1: {sum([len(x) for x in list_of_union_answer])}')

# part 2
input = [x.split('\n') for x in input]


def get_list_of_sets(input):
    out = []
    for group in input:
        elem_list = []
        for person in group:
            elem_list.append(set(get_list_of_characters(person)))
        out.append(elem_list)
    return out


def get_intersections(input):
    out = []
    for group in input:
        intersect = group[0]
        for person in group:
            intersect = intersect.intersection(person)
        out.append(intersect)
    return out


list_of_intersecting_answers = get_intersections(get_list_of_sets(input))
print(f'Solution for part 2: {sum([len(x) for x in list_of_intersecting_answers])}')
