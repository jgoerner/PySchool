# Decorating a function that takes arguments
## Description
In contrast to the [simple Decorator](https://github.com/jgoerner/PySchool/blob/master/02-decorators/recipes/Decorator_simple.md) 
the following requirements need to be fulfilled in order to decorate a 
function that takes an arbitrary number of (keyword) arguments:
- extend the internal `wrapper` method signature to accept `*args` and `**kwargs` parameter
- inside the internal `wrapper` execute the original function with the parameter `*args` and `**kwargs`

## Example
The following example can be found unter [src/decorator_with_parameter.py](https://github.com/jgoerner/PySchool/blob/master/02-decorators/recipes/src/decorator_with_parameter.py).
```python
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
```
