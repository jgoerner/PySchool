# Package Building
As a final step the a Python package needs to be "built" in order to be provided on the Python Packaging Index (PyPI).
The following sections briefly explain the issues to consider.

## Configuration with *setuptools*
The foundation for the correct building is a `setup.py` file that contains information like the name, a short description, 
but also the list of modules/packages to include. Detailled information about all parameter of the setup.py can be 
found at the [official documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use). 
The following depicts an example for a setup.py:
```python
from setuptools import setup, find_packages

setup(name="jgoerner-greetings",
      version="1.0",
      description="A small weekend project without a deeper usage",
      packages=find_packages(),
      setup_requires=["pytest-runner"],
      tests_require=["pytest"]
      )
```

## Building a source distribution
There are two kinds of distributions that can be built. The first (and deprecated one) is a source package. 
To build a source package one has to run the following command:
```
python setup.py sdist
```
This will create a bundled .tar.gz in the `dist/` directory. 

## Building a Python wheel
A Python [wheel](http://pythonwheels.com) is the second and recommended kind of distribution - esp. since it does not involve further
building once downloaded. In order to build a Python wheel one has to run the following command:
```
python setup.py bdist_wheel --universal
```
The wheel is also put into the `dist/` directory. It has to be said, that the previous command assumed, 
that the package contains only Python code that is compatible with Python 2.x and 3.x. For more information
the [official documentation](http://pythonwheels.com) should be read.

## Uploading the package with *twine*
In order to upload the built packages the usage of twine is recommended since it uses HTTPS and deliveres
the built in a secure manner to the target repository site. In order to upload the built package one has to run:
```
twine upload -repository-url https://test.pypi.org/legacy/ dist/*
```
Note that this command uploads the package only to the test version of PyPI (registration 
is necessary!).
