#!/usr/bin/python3

import os,sys


def tail_file(filename, nlines):
    with open(filename) as f:
        f.seek(0, os.SEEK_END)
        endf = position = f.tell()

        linecnt = 0
        while position >= 0:
            f.seek(position)
            c = f.read(1)
            if c == "\n" and position != endf-1: 
                linecnt += 1

            if linecnt == nlines:
                break
            position -= 1

        if position < 0:
            f.seek(0)

        print(f.read(),end='')


if __name__ == '__main__':
    filename = sys.argv[1]
    nlines = int(sys.argv[2])
    tail_file(filename, nlines)
