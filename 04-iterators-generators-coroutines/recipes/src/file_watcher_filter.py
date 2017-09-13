import time
import os
import sys


def watch(f):
    """
    Watching the file f and print changes
    """
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, pattern="WARNING"):
    for line in lines:
        if pattern in line:
            yield line

if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(os.path.join(os.getcwd(), sys.argv[-1]))
        f_lines = watch(f)
        pattern_lines = grep(lines=f_lines)
        for line in pattern_lines:
            print(line)
