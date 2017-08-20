# Weekend Project "Packaging" :gift:

## Technical Requirements
This weekend's project should wrap up the topic of python packaging including 
aspects of "modern" software engineering. The following themes shall be covered:

- [X] Source Control ([Git](https://git-scm.com), [GitHub](https://github.com))
- [X] Testing ([pytest](https://docs.pytest.org/en/latest/), [Makefile](https://www.gnu.org/software/make/manual/make.html), [Travis CI](https://travis-ci.org))
- [X] Code Coverage ([pytest-cov](https://pypi.python.org/pypi/pytest-cov), [coveralls.io](https://coveralls.io/
), [codecov.io](https://codecov.io))
- [X] Code Styling ([flake8](http://flake8.pycqa.org/en/latest/), [autopep8](https://pypi.python.org/pypi/autopep8), [Better Code Hub](https://bettercodehub.com))
- [X] Continuous Integration ([Travis CI](https://travis-ci.org))
- [X] Documentation ([reStructuredText](http://docutils.sourceforge.net/rst.html), [Sphinx](http://www.sphinx-doc.org/en/stable/), [Read the docs](https://readthedocs.org))
- [ ] Providing the package on PyPI (test version)

## Content of the Package
The package to be developed deals with greeting people in different languages. The output should somehow look like that:
```python
# English
greet("Joshua", "EN")
"Hello Joshua, how are you today?"

# Deutsch
greet("Joshua", "DE")
"Hallo Joshua, wie geht es dir heute?"
```

## Greetings
Sourcecode: [@GitHub](https://github.com/jgoerner/greetings)<br>
Documentation: [@Read The Docs](http://jgoerner-greetings.readthedocs.io/en/latest/)<br>
Package: [@Test PyPI](https://testpypi.python.org/pypi/jgoerner-greetings/1.0)<br>
Badges:<br>
[![Build Status](https://travis-ci.org/jgoerner/greetings.svg?branch=master)](https://travis-ci.org/jgoerner/greetings)
[![Coverage Status](https://coveralls.io/repos/github/jgoerner/greetings/badge.svg?branch=master)](https://coveralls.io/github/jgoerner/greetings?branch=master)
[![codecov](https://codecov.io/gh/jgoerner/greetings/branch/master/graph/badge.svg)](https://codecov.io/gh/jgoerner/greetings)
[![BCH compliance](https://bettercodehub.com/edge/badge/jgoerner/greetings?branch=master)](https://bettercodehub.com/)
[![Documentation Status](https://readthedocs.org/projects/jgoerner-greetings/badge/?version=latest)](http://jgoerner-greetings.readthedocs.io/en/latest/?badge=latest)
