SHAPE_MAP = {'A': 'X', 'B': 'Y', 'C': 'Z'}
SHAPE_VALUES = {'X': 1, 'Y': 2, 'Z': 3}
LOSING_SHAPES = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
WINNING_SHAPES = {'Z': 'X', 'X': 'Y', 'Y': 'Z'}


def get_input():
    with open("input.txt") as i:
        return [line.rstrip('\n') for line in i]


def get_rounds():
    return [r.split(' ') for r in get_input()]


def get_opponent_shape(marker):
    return SHAPE_MAP[marker]


def get_losing_shape(shape):
    return LOSING_SHAPES[shape]


def get_shape_value(shape):
    return SHAPE_VALUES[shape]


def get_round_score(player_hand, opponent_hand):
    if get_losing_shape(player_hand) is opponent_hand:
        return 6
    elif player_hand is opponent_hand:
        return 3
    else:
        return 0


def get_required_shape(opponent_hand, result):
    if result == 'X':
        return LOSING_SHAPES[opponent_hand]
    elif result == 'Z':
        return WINNING_SHAPES[opponent_hand]
    else:
        return opponent_hand


if __name__ == '__main__':
    # step 1
    print(sum([get_round_score(r[1], get_opponent_shape(r[0])) + get_shape_value(r[1]) for r in get_rounds()]))
    # step 2
    print(sum([
        get_round_score(get_required_shape(get_opponent_shape(r[0]), r[1]), get_opponent_shape(r[0])) +
        get_shape_value(get_required_shape(get_opponent_shape(r[0]), r[1])) for r in get_rounds()]))
