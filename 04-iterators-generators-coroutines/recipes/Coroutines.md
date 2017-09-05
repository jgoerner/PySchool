# Coroutine
## Definition
Coroutines and Generators are closely related. Per definition a `generator` is a special kind of `coroutine`.
In contrast to simple generators, coroutines can also consume values throughout their lifetime by using the syntax:

```python3
# inside coroutine
value = yield result
...

# outisde the coroutine
my_coroutine.send(value)
...
```

Using the `send()` method of a coroutine will injest the parameter (`value`) into the coroutine, which will yield the `result` 
variable.

## Example Usage
The following coroutine

```python
def stats_coroutine():
    sum = avg = items = 0
    yield  # initial stop
    while True:
        increment = yield sum, avg
        sum += increment
        items += 1
        avg = sum / items
```

can be used as follows:

```python
counter = stats_coroutine()
next(counter)  # initialize the coroutine
for _ in range(5):
    print(counter.send(random.randint(0, 10)))
    
>>> (0, 0)
>>> (9, 9.0)
>>> (19, 9.5)
>>> (25, 8.333333333333334)
>>> (33, 8.25)
```
