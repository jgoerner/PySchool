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

## Code coverage automation with *make*
In order to (semi) automate the coverage calculation, the python commands above 
can be also put into a Makefile - [like the automated testing procedure](https://github.com/jgoerner/PySchool/blob/master/01-packaging/recipes/Testing.md#automating-testing-with-make)

## Code coverage automation with *coveralls.io*
[Coveralls.io](https://coveralls.io) is a web based service that automatically checks the code coverage. For open source projects Coveralls offers a free tier option. Take the following steps to enable the coverage report with coverall.io:
1) Register on [coverall.io](https://coveralls.io)
2) Go to settings and enable the coverage report for the according repository
3) Make sure your .travis.yml includes the following lines
```
install:
    - pip install pytest-cov coveralls

script:
    - python -m pytest --cov=./ 

after_success:
    - coveralls 
```
4) Commit and push to your codebase

Here is an example of a coveralls dashboard<br><br>
![coveralls demo](https://coveralls.io/assets/home_screen-a4d6ff047dc0c195a77394c64c35a5443a10d11ace900070a92604fd9d468256.jpg)

## Code coverage automation with *codecov.io*
[codecov.io](https://codecov.io/) is a web based service that automatically checks the code coverage. For open source projects codecov offers a free tier option. Take the following steps to enable the coverage report with coverall.io:
1) Register on [https://codecov.io/](https://codecov.io/)
2) Go to settings and enable the coverage report for the according repository
3) Make sure your .travis.yml includes the following lines
```
install:
    - pip install pytest-cov codecov

script:
    - python -m pytest --cov=./ 

after_success:
    - codecov 
```
4) Commit and push to your codebase

Here is an exaple of a codecov dashboard<br><br>
![codecov demo](http://d2.alternativeto.net/dist/s/codecov-io_571229_full.png?format=jpg&width=1600&height=1600&mode=min&upscale=false)
