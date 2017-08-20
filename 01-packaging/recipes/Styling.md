# Code Styling
Code Styling plays a major role in Pyhton. Missing or wrong indents can lead to non working code. 
The [Python Enhancement Proposals #8 (PEP8)](https://www.python.org/dev/peps/pep-0008/) define a 
common styleguide on how to write Python code, including topics like indention, naming conventions,
comments and much more. In addition to this document the [PEP 257](https://www.python.org/dev/peps/pep-0257/)
provides recommendations about Docstrings. 

## Checking Code Styling with *flake8*
[Flake8](http://flake8.pycqa.org/en/latest/index.html) is a command-line utility for enforcing style consistency across Python projects. 
By default it includes lint checks provided by the PyFlakes project, PEP-0008 inspired style checks provided by the 
PyCodeStyle project, and McCabe complexity checking provided by the McCabe project. Flake8 will procude a list of 
code lines, that not comply with the styleguides mentioned above. To run the stylecheck against the current directory
simply type:
```
flake8 .
```
If no violation was found, the result will be empty. If errors are found the reuslt should look like this:
```
./greetings/greeter.py:3:14: E225 missing whitespace around operator
./greetings/greeter.py:7:1: E302 expected 2 blank lines, found 1
./greetings/greeter.py:20:80: E501 line too long (81 > 79 characters)
```

## Checking & enforcing Code Styling with *autopep8*
[Autopep8](https://pypi.python.org/pypi/autopep8) automatically changes the code to comply with the
[PEP8](https://www.python.org/dev/peps/pep-0008/) styleguides. In order to change all the .py files in the 
current directory and all subdirectories, the following command shall be executed:
```
autopep8 --in-place --recursive . --agressive --agressive
```
The `--agressive` flag can be set multiple times and determines the severity of errors that autopep8 will fix.

## Automate checking and enforcing Code Styling with *make*
In order to (semi) automate the stly checking, the python commands above can be also put into a Makefile - 
like the [automated testing procedure](https://github.com/jgoerner/PySchool/blob/master/01-packaging/recipes/Testing.md#automating-testing-with-make).

## Automated Checking Code Styling with *bettercodehub*
[Bettercodehub](https://bettercodehub.com/) is a web service that automatically checks the code quality after each
push to GitHub. The checks are based on [Building Maintainable Software](http://shop.oreilly.com/product/0636920049159.do)
and include the following "mantras":
1. Write short units of code
2. Write simple units of code
3. Write code once
4. Keep unit interface small
5. Separate concers in modules
6. Couple architecture components lousely
7. Kepp architecture components balanced
8. Keep your codebase small
9. Automate tests
10. Writen clean code

Once registered and logged in, one has to enable the repository for an initial code checking.
In addition to that under the repository settings the toggle *push & pull request analysis*
shall be turned on.
