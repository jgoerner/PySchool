#!/usr/bin/env python
import random

def stats_coroutine():
    sum = avg = items = 0
    yield  # initial stop
    while True:
        increment = yield sum, avg
        sum += increment
        items += 1
        avg = sum / items


if __name__ == "__main__":
    counter = stats_coroutine()
    next(counter)  # initialize the coroutine
    for _ in range(10):
        print(counter.send(random.randint(0, 10)))
