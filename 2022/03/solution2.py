from functools import reduce


def main(f):
    total = 0
    while True:
        line1 = f.readline().strip()
        if line1 is None or len(line1) == 0:
            break
        line2 = f.readline().strip()
        line3 = f.readline().strip()
        res = list(reduce(lambda i, j: i & j, (set(x)
                    for x in [line1, line2, line3])))
        score = ord(res[0]) - (96 if res[0].islower() else 38)
        total += score
    print(total)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
