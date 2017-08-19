# Code Coverage
As explained in the [Testing](https://github.com/jgoerner/PySchool/blob/master/01-packaging/recipes/Testing.md) page, automated tests have a high influence
on improving ones source code. But there is more to the picture than just 
having tests that pass. A crucial indicator "how much code" the tests cover
is the so called code coverage. A high code coverage mostly indicates
high quality code - "mostly" because just having non-sense tests, that cover 
almost the complete codebase will improve the code coverage but not the code
quality.

## Code coverage with *pytest-cov*
[]() is an addition to pytest that also includes the calculation of
code coverage statistics. Once installed it can be invoked by the following command
```
python -m pytest --cov tests/
```
This shall give a CLI representation of the tested code, included how many lines
are covered and how many are missed. Here is an example.
```
============================= test session starts ==============================
platform darwin 
-- Python 3.5.2, pytest-3.0.6, py-1.4.34, pluggy-0.4.0
rootdir: /Users/joshuagorner/Desktop/greetings, inifile: 
plugins: cov-2.5.1
collected 4 items

tests/test_greeter.py ....

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
greetings/__init__.py       0      0   100%
greetings/greeter.py        6      0   100%
tests/test_greeter.py      12      0   100%
-------------------------------------------
TOTAL                      18      0   100%


=========================== 4 passed in 0.04 seconds ===========================
```
Another very handy feature of pytest-cov is the formatted output as a bundle of 
HTML files. The follwing command will calculate the code coverage and export
the statistics into a nicely formatted webpage.
```
python -m pytest --cov --cov-report html:cov_html tests/
```
The HTML reports are all interactive and linked, which makes it extremely user-friendly.
The following images depict sample HTML coverage reports.<br><br>
![HTML coverage overview](https://i.stack.imgur.com/UOnur.png)<br>
![HTML coverage report](http://oddbird.net/python-testing-tools-preso/images/coverage.png)

## Automated code coverage with *make*
In order to (semi) automate the coverage calculation, the python commands above 
can be also put into a Makefile - [like the automated testing procedure](https://github.com/jgoerner/PySchool/blob/master/01-packaging/recipes/Testing.md#automating-testing-with-make)

# TODO: REFACTOR FROM HERE

## Code coverage with coveralls.io
[Coveralls.io]() is a web based service that automatically checks the code coverage. For open source projects Coveralls 
offers a free tier option. Once logged in with the GitHub credentials one has to 
enable the according repository in the coveralls settings. After the next commit, 
coveralls will procude metrics like the following:

## Code coverage with codecov.io
