#!/usr/bin/env python


def name_decorator(func):

    def wrapper(*args, **kwargs):
        print("{} was executed with the params {} {}".format(func.__name__,
                                                             args, kwargs))
        return func(*args, **kwargs)

    return wrapper


@name_decorator
def say_hello(name, age):
    print("Hello {} ({} old)".format(name, age))


if __name__ == "__main__":
    say_hello("Bob", age=26)
