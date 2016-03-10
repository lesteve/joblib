import subprocess
import string
import sys
import re
import itertools
import os

# FILENAME = '/home/le243287/test.out'
FILENAME = '/tmp/test.out'
NB_WRITERS = 20
LINE_LENGTH = int(sys.argv[1])
NB_LINES_PER_WRITER = 50

if os.path.exists(FILENAME):
    os.unlink(FILENAME)

processes = [subprocess.Popen('python writer.py {} {} {} {}'.format(
    FILENAME, letter, LINE_LENGTH, NB_LINES_PER_WRITER).split())
    for _, letter in zip(range(NB_WRITERS),
                         itertools.cycle(string.ascii_letters))]

for p in processes:
    p.wait()

pattern = r'(.)\1{{{}}}$'.format(LINE_LENGTH - 1)


nb_lines = sum(1 for _ in open(FILENAME))
assert nb_lines == NB_LINES_PER_WRITER * NB_WRITERS

with open(FILENAME) as fp:
    non_matching_lines = [line for line in fp
                          if not re.match(pattern, line)]

print(''.join(non_matching_lines[:20]))
