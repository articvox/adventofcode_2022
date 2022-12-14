import string
from itertools import islice


def get_input():
    with open("input.txt") as i:
        return [line.rstrip('\n') for line in i]


def compartmentalize(rucksack):
    return [rucksack[:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):]]


def find_duplicate(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item


def grouped(rucksacks):
    it = iter(rucksacks)
    while True:
        group = list(islice(it, 3))
        if not group:
            return None
        yield group


def contains(rucksacks, item):
    for rucksack in rucksacks:
        if item not in rucksack:
            return False
    return True


def find_badge(rucksacks):
    for item in rucksacks.pop():
        if contains(rucksacks, item):
            return item


if __name__ == '__main__':
    # step 1
    print(sum(string.ascii_letters.find(find_duplicate(*compartmentalize(i))) + 1 for i in get_input()))

    # step 2
    print(sum(string.ascii_letters.find(find_badge(g)) + 1 for g in grouped(get_input())))
