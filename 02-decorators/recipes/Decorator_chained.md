# Chaining multiple Decorator
## Description
In contrast to the [simple Decorator](https://github.com/jgoerner/PySchool/blob/master/02-decorators/recipes/Decorator_simple.md)
the following requirements need to be fulfilled in order to chain multiple decorators in a clean manner:
- import the function `wraps` from the `functools` module
- decorate each internal `wrapper` with the `@wraps(original_function)`

## Example
The following example can be found under (src/decorator_chained.py)[https://github.com/jgoerner/PySchool/blob/master/02-decorators/recipes/src/decorator_chained.py].
```python
#!/usr/bin/env python
import time
from functools import wraps


def name_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("{} was executed with the params {} {}".format(func.__name__,
                                                             args, kwargs))
        return func(*args, **kwargs)

    return wrapper


def time_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        time.sleep(2)
        t2 = time.time()
        print("{} ran {} seconds".format(func.__name__, t2 - t1))
        return result

    return wrapper


@time_decorator
@name_decorator
def say_hello(name, age):
    print("Hello {} ({} old)".format(name, age))


if __name__ == "__main__":
    say_hello("Bob", age=26)
```
