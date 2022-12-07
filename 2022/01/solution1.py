def main(f):
    total = 0
    highest = 0
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            if total > highest:
                highest = total
            total = 0
            continue
        total += int(line)
    if total > highest:
        highest = total
    print(highest)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
