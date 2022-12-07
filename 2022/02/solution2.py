translation = {'A': 'R', 'B': 'P', 'C': 'S'}
win = {'R': 'S', 'P': 'R', 'S': 'P'}
lose = {'R': 'P', 'P': 'S', 'S': 'R'}
points = {'R': 1, 'P': 2, 'S': 3}


def main(f):
    total = 0
    for line in f.readlines():
        opponent, outcome = line.strip().split(' ')
        opponent = translation[opponent]
        if outcome == 'X':
            me = win[opponent]
        elif outcome == 'Y':
            me = opponent
        elif outcome == 'Z':
            me = lose[opponent]

        # Calculate points
        result = 0
        if opponent == me:
            result = 3
        elif win[opponent] != me:
            result = 6
        total += points[me] + result
    print(total)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
