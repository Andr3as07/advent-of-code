import sys


def main(f):
    WINDOW_SIZE = 14
    for line in f.readlines():
        line = line.strip()
        for i in range(len(line)-WINDOW_SIZE):
            buffer = line[i:i+WINDOW_SIZE]
            if len(list(set(buffer))) == len(buffer):
                print(i+WINDOW_SIZE)
                break


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
