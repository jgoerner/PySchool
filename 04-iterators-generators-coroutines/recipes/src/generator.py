#!/user/bin/env python
import random


def random_int_generator(lower=0, upper=10):
    while True:
        yield random.randint(lower, upper)


if __name__ == "__main__":
    my_gen = random_int_generator()
    for _ in range(10):
        print(next(my_gen))
