def main(f):
    highest = []
    total = 0
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            highest.append(total)
            total = 0
            continue
        total += int(line)
    highest.append(total)
    highest.sort()
    print(sum(highest[-3:]))


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
