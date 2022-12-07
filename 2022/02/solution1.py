translation = {'A': 'R', 'B': 'P', 'C': 'S',
               'X': 'R', 'Y': 'P', 'Z': 'S'}
win = {'R': 'S', 'P': 'R', 'S': 'P'}
points = {'R': 1, 'P': 2, 'S': 3}


def main(f):
    total = 0
    for line in f.readlines():
        opponent, me = line.strip().split(' ')
        opponent = translation[opponent]
        me = translation[me]

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
