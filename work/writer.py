import time
import sys


def main():
    filename, letter, length, nb_lines_per_writer = sys.argv[1:]
    length = int(length)
    nb_lines_per_writer = int(nb_lines_per_writer)
    with open(filename, 'a') as fp:
        to_write = letter * length + '\n'
        for _ in range(nb_lines_per_writer):
            time.sleep(0.1)
            fp.write(to_write)


if __name__ == '__main__':
    main()
