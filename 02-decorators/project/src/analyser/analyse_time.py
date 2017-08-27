from functools import wraps
from collections import defaultdict
import time
import os
import atexit
import inspect

exec_module = None


def analyse_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        global exec_module
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        exec_module = inspect.getmodule(function)
        exec_function = function.__name__
        # check if module already has a dict
        try:
            exec_module.logged_functions[exec_function] += (t1 - t0)
        except AttributeError:
            exec_module.logged_functions = defaultdict(float)
            exec_module.logged_functions[exec_function] += (t1 - t0)
        return result
    return wrapper


@atexit.register
def goodbye():
    with open(os.path.join(os.getcwd(), "LOG.txt"), "w") as file:
        file.write("FUNCTION \t TIME\n")
        for func, runtime in exec_module.logged_functions.items():
            file.write("{} \t {:.5f}\n".format(func, runtime))
