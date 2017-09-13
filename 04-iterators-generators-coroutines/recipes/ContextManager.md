# ContextManager

## Definition
> Python’s with statement supports the concept of a runtime context defined by a context manager. This is implemented using two separate methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends. The context management protocol consists of a pair of methods that need to be provided for a context manager object to define a runtime context.

One example built-in context manager is provided by *open*:
```python
with open("text.txt") as file:
  file.readlines()
  ...
```


## Example Usage
A contextmanager can be created by utilising the *contextmanager* decorator.
```python
import tempfile, shutil
from contextlib import contextmanager

@contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()
    try:
        yield outdir
    finally:
        shutil.rmtree(outdir)
```
This contextmanager creates a temporary directory and deletes it after leaving the context:
```python
with tempdir() as t:
  t.extract_large_file() // or other fancy function
  ...
```
