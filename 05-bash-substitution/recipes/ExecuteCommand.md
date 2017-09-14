# Execute a BASH command
In order to execute a BASH command from within Python, the module `subprocess` is recommended.
The following code depicts a simple method to run passed BASH commands.
```python
import subprocess


def execute_command(cmd):
    """
    Execute the passed command
    """
    subprocess.call(cmd.split())


if __name__ == "__main__":
    execute_command("ls -a /usr")
```
This will lead to the output
```
>>> foo/  bar/  sample/ dir/
```
