from parse import parse


def main(f):
    board = []

    # Initial State
    while True:
        line = f.readline()
        if line.startswith(" 1"):
            break
        llen = len(line)
        index = 1
        lane = 0
        while index < llen:
            symbol = line[index]
            if len(board) <= lane:
                board.append([])
            if symbol != ' ':
                board[lane].append(symbol)
            index += 4
            lane += 1

    # Skip empty line
    f.readline()

    # Move around
    for line in f.readlines():
        line = line.strip()
        result = parse('move {:d} from {:d} to {:d}', line)
        amt, src, dst = result.fixed

        payload = board[src-1][:amt]
        payload = payload[::-1]
        board[src-1] = board[src-1][amt:]
        payload.extend(board[dst-1])
        board[dst-1] = payload

    # Get top
    top = ""
    for i in range(len(board)):
        top += board[i][0]
    print(top)


if __name__ == '__main__':
    import sys
    with open('input.txt' if len(sys.argv) > 1 and sys.argv[1] == '-r' else 'example-input.txt') as f:
        main(f)
