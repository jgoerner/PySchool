# A basic Decorator
## Description
A basic decorator consists of the following parts:
- a method signature, that accepts the `original_function`
- an internal wrapper function that executes the original function and adds some extra functionality
- a return statement that returns the internal wrapper

## Example
The following code can be found under [src/decorator_simple.py](https://github.com/jgoerner/PySchool/blob/master/02-decorators/recipes/src/decorator_simple.py).
```python 
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
```
