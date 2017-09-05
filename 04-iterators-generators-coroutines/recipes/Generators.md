# Generators
## Textbook Definition
A Python generator is a function which returns a generator iterator 
(just an object we can iterate over) by calling `yield`. `yield` may be called with a value, 
in which case that value is treated as the "generated" value. The next time `next()` is 
called on the generator iterator (i.e. in the next step in a `for` loop, for example),
the generator resumes execution from where it called `yield`, not from the beginning of the function. 
All of the state, like the values of local variables, is recovered and the generator contiues to execute 
until the next call to `yield`. 
([source of definition](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/))

## Example Usage
The generator
```python
#!/user/bin/env python
import random


def random_int_generator(lower=0, upper=10):
    while True:
        yield random.randint(lower, upper)
```
can be use as follows:
```python
my_gen = random_int_generator()
    for _ in range(10):
        print(next(my_gen))

>>> 9
>>> 3
>>> 3
>>> 8
>>> 7
>>> 0
>>> 4
>>> 5
>>> 1
>>> 1
```
