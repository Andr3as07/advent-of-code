from functools import reduce


def main(f):
    total = 0
    for line in f.readlines():
        line = line.strip()
        length = len(line)
        a = line[:length//2]
        b = line[length//2:]
        res = list(reduce(lambda i, j: i & j, (set(x) for x in [a, b])))[0]
        score = ord(res) - (96 if res.islower() else 38)
        total += score
    print(total)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
