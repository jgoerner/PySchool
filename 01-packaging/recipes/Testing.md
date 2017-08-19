# Testing
In order to ensure high quality right from the beginning, 
it is recommended to test the source code automatically.
Simple yet sufficient recipes are listed below.

## Folder Structure
In order to bundle all test, one should create a *tests* directory in the root
of the project. Inside of this dir, test modules can be created which contain
the concrete test scripts. **It is key that all the modules and all the test
methods have the prefix 'test' - if not, pytest wont include them.**
Here is an example of a simple test-setup:


    ├── mymodule                   
    │   ├── __init__.py 
    │   └── mymodule.py             <- written python code
    │
    └── tests                       
        ├── test_my_code.py         <- test module
        ├── test_other_code.py
        └── more_testing.py
        
```python
# inside test_my_code.py

def test_hello_word():
  assert mymodule.say_hello() == "Hello World"
  
def test_bye_bye():
  assert mymodule.say_bye() == "Bye Bye"
```     

## Testing with *pytest*
[Pytest](https://docs.pytest.org/en/latest/) is a quite handy tool when it comes 
to testing. Once executed from the CLI pytest will automatically search 
for tests and run them (iff suffix '*test*' was used). Being in the root of the 
project, pytest can be invoked as follows:
```
python -m pytest tests/ -v
```
If all tests pass, the result should look like this:
```
============================= test session starts ==============================
platform darwin 
-- Python 3.5.2, pytest-3.0.6, py-1.4.34, pluggy-0.4.0 
-- /Users/joshuagorner/anaconda/bin/python
cachedir: .cache
rootdir: /Users/joshuagorner/Desktop/delete, inifile: 
plugins: cov-2.5.1
collecting ... collected 2 items

tests/test_my_module.py::test_hello_world PASSED
tests/test_my_module.py::test_bye_bye PASSED

=========================== 2 passed in 0.01 seconds ===========================
```
If one (or more) test fails, pytest will also record this information.

## Automating testing with *make*
In order to (semi) automate the testing procedure (and not having to call 
`python -m pytest -v tests/` all the time) one can take advantage of
[Makefiles](https://www.gnu.org/software/make/manual/make.html). 
Here is an example of a fairly simple Makefile, that eases the 
testing workflow.
```
# MAKEFILE
test:
  python -m pytest -v tests/
```
Having this Makefile allows for the following CLI command, which will exactly result
in the same test execution as before.
```
make test
```
A great advantage of Makefiles is, that their so called 'targets' (in this case the 
target has the name 'test') can be put together in execution dependencies. E.g. one
could enforce to make tests before other targets (like a commit) are executed.

## Automating testing with TravisCI
[TravisCI](https://travis-ci.org) is one (out of dozen) so called 
'continuous integration' web services.The basic principle behind Travis 
(and other CIs) is to get notified, whenenver a new commit was pushed to the codebase. 
Automating with a CI provider works slightly different compared to the 
latter approach but is still not overy complex. In order to enable TravisCI, one has to
1. Register on [https://travis-ci.org](https://travis-ci.org) 
and link with ones GitHub account
2. Explicitly enable the CI integration in the travis settings for the given repository
3. Add a '.travis.yml' file to the project directory, containing the following code
```
language: python

python:
  - "3.5"

script:
  - python -m pytest -v tests/
```
4. Commit and push the code to GitHub

