# Weekend Project "Decorators" :guardsman:

## The Decorator Requirements
The decorator to be build shall log the runtime of all executed decorated functions
and create a log file at the end of a programm run containing the cumulated runtimes.

```python
################
# my_module.py #
################

# first decorated method
@analyse_time
def foo():
  ...

# another decorated method
@analye_time
def bar()
  ...
  
  
###########
# Log.txt #
###########

Function  Time
foo       0:10
bar       0:15
```
**Optional**<br>
Enhance the decorator to accept the arguments *t* and *p*. If *t* is set, the decorator
will work just as described above and log the times. If *p* is set the decorator will
track all parameters that were passed to that function.
