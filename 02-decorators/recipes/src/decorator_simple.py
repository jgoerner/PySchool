#!/usr/bin/env python


def name_decorator(func):

    def wrapper():
        print("{} was executed...".format(func.__name__))
        return func()

    return wrapper


@name_decorator
def say_hello():
    print("Hello World")


if __name__ == "__main__":
    say_hello()
