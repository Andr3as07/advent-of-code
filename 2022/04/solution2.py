def overlaps(a, b):
    al = int(a[0])
    ah = int(a[1])
    bl = int(b[0])
    bh = int(b[1])
    for i in range(min(al, bl)-1, max(ah, bh)+1):
        if i >= al and i <= ah and i >= bl and i <= bh:
            return True
    return False


def main(f):
    counter = 0
    for line in f.readlines():
        line = line.strip()
        parts = line.split(',')
        a = parts[0].split('-')
        b = parts[1].split('-')
        if overlaps(a, b):
            counter += 1
    print(counter)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
