def contains(a, b):
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])


def main(f):
    counter = 0
    for line in f.readlines():
        line = line.strip()
        parts = line.split(',')
        a = parts[0].split('-')
        b = parts[1].split('-')
        if contains(a, b) or contains(b, a):
            counter += 1
    print(counter)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
