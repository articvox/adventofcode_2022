from itertools import groupby


def get_input():
    with open("input.txt") as i:
        return [line.rstrip('\n') for line in i]


if __name__ == '__main__':
    calories = [list([int(cal) for cal in group]) for key, group in groupby(get_input(), lambda x: x == '') if not key]
    print(max([sum(group_calories) for group_calories in calories]))
