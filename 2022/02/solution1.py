def get_reward(opponent: str, me: str):
    if opponent == 'A':
        if me == 'X':
            return 3
        elif me == 'Y':
            return 6
        elif me == 'Z':
            return 0
        assert False, "unreachable"
    elif opponent == 'B':
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        elif me == 'Z':
            return 6
        assert False, "unreachable"
    elif opponent == 'C':
        if me == 'X':
            return 6
        elif me == 'Y':
            return 0
        elif me == 'Z':
            return 3
        assert False, "unreachable"
    assert False, "unreachable"


def main(f):
    points = {'X': 1, 'Y': 2, 'Z': 3}
    total = 0
    for line in f.readlines():
        opponent, me = line.strip().split(' ')
        result = get_reward(opponent, me)
        score = points[me] + result
        total += score
    print(total)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
