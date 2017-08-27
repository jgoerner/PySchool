#!/bin/usr/env python
from analyser.analyse_time import analyse_time
import time


@analyse_time
def printer(text, delay):
    for c in text:
        print(c)
        time.sleep(delay / len(text))


@analyse_time
def summator(a, b):
    return a + b


if __name__ == "__main__":
    printer("Hello World", 3)
    print(summator(1234, 5678))
    printer("Foo Bar", 2)
    print(summator(11223344, 55667788))
    printer("Everybody was kungfu fighting", 5)
