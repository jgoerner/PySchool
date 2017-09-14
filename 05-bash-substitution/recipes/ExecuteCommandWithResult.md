# Execute a BASH command and retrieve the result
In order to run a BASH command and further work on the result of that command, the class `Popen` is recommended.
The following snippet depicts a method to run a BASH command and retrieve the result.
```python
import subprocess


def execute_command_with_return(cmd):
    """
    Execute a command and return the result as a list
    """
    process = subprocess.Popen(cmd.split(),
                               stdout=subprocess.PIPE)
    out, _ = process.communicate()
    result = [line.decode("utf-8") for line in out.split()]
    return result


if __name__ == "__main__":
    items = execute_command_with_return("ls -a /usr")
    print(items)
```
This method will return the items in a list like:
```
>>> ['foo', 'bar', 'sample', 'dir']
```
