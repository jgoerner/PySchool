# Code Documentation
Creating a documentation increases the value of the code but is very often tedious to do. The following tools 
shall help with creating & maintaining a valuable documentation

## Creating the Documentation with *sphinx*
[Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is a documentation generator for python. Since sphinx has dozens of plugins and option, only the very basic 
configuration shall be shown here. For more details the [getting started guide](http://www.sphinx-doc.org/en/stable/tutorial.html)
is recommended. In order to create a basic sphinx documentation:
1. run ```pip install sphinx```
2. create a docs/ dir in the project
3. navigate into to docs/ dir and run
```sphinx-quickstart```
4. provide (at least the mandatory) information, skip default with <enter>
5. run ```make html``` to build the first (and empty) version of the documentation 
which can be accessed under the ```./docs/_build/``` path.
6. assuming that a documenting .rst file calles sample_doc.rst already exists, configure the ```index.rst``` and add 
the following lines:
```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
                              <- add a blank line here
   sample_doc                 <- add the name (without .rst)
```
**Be aware that a blank line needs to be added first and all indentation is equal to 3 whitespaces**.

## Managing & Hosting the Documentaton with *read the docs*
[Read the Docs](https://readthedocs.org) is a webservice, that hosts documentation, 
making it fully searchable and easy to find. In addition also downloads as e.g. PDF are fully available.
Once signed up & logged in, one has to perform he following steps.
1. Go to "settings" and link ones GitHub account
2. Import the wanted repository
3. Run "build" under the "overview" menu
4. The hosted documentation shall now be available
