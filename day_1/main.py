from itertools import groupby


def get_input():
    with open("input.txt") as i:
        return [line.rstrip('\n') for line in i]


if __name__ == '__main__':
    # step 1
    calories = [list([int(cal) for cal in group]) for key, group in groupby(get_input(), lambda x: x == '') if not key]
    total_calories = [sum(group_calories) for group_calories in calories]
    print(max(total_calories))

    # step 2
    print(sum(sorted(total_calories, reverse=True)[:3]))
