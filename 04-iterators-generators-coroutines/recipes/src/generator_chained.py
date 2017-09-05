#/usr/bin/env python
from generator import random_int_generator

def meta_generator(lower=0, upper=10, n_gen=3):
    generators = [random_int_generator(lower, upper)
                  for _ in range(n_gen)]
    yield from zip(*generators)


if __name__ == "__main__":
    mg = meta_generator(n_gen=10)
    for _ in range(5):
        print(next(mg))
