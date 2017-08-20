# Weekend Project "Packaging" :gift:

## Technical Requirements
This weekend's project should wrap up the topic of python packaging including 
aspects of "modern" software engineering. The following themes shall be covered:

- [X] Source Control ([Git](https://git-scm.com), [GitHub](https://github.com))
- [X] Testing ([pytest](https://docs.pytest.org/en/latest/), [Makefile](https://www.gnu.org/software/make/manual/make.html), [Travis CI](https://travis-ci.org))
- [X] Code Coverage ([pytest-cov](https://pypi.python.org/pypi/pytest-cov), [coveralls.io](https://coveralls.io/
), [codecov.io](https://codecov.io))
- [X] Code Styling ([flake8](http://flake8.pycqa.org/en/latest/), [autopep8](https://pypi.python.org/pypi/autopep8), [Better Code Hub](https://bettercodehub.com))
- [X] Continuous Integration ([Travis CI](https://travis-ci.org)
- [ ] Documentation
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
