You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/hbarrett/ckan-wdi-theme.svg?branch=master
    :target: https://travis-ci.org/hbarrett/ckan-wdi-theme

.. image:: https://coveralls.io/repos/hbarrett/ckan-wdi-theme/badge.svg
  :target: https://coveralls.io/r/hbarrett/ckan-wdi-theme

.. image:: https://pypip.in/download/ckan-wdi-theme/badge.svg
    :target: https://pypi.python.org/pypi//ckan-wdi-theme/
    :alt: Downloads

.. image:: https://pypip.in/version/ckan-wdi-theme/badge.svg
    :target: https://pypi.python.org/pypi/ckan-wdi-theme/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckan-wdi-theme/badge.svg
    :target: https://pypi.python.org/pypi/ckan-wdi-theme/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckan-wdi-theme/badge.svg
    :target: https://pypi.python.org/pypi/ckan-wdi-theme/
    :alt: Development Status

.. image:: https://pypip.in/license/ckan-wdi-theme/badge.svg
    :target: https://pypi.python.org/pypi/ckan-wdi-theme/
    :alt: License

=============
ckan-wdi-theme
=============

Bootstrap theme for CKAN

------------
Requirements
------------

In development for 2.8


------------
Installation
------------
WARNING!
This addon is still in development!
Use at your onw risk!



To install ckan-wdi-theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckan-wdi-theme Python package into your virtual environment::

     pip install ckan-wdi-theme

3. Add ``wdi_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.wdi_theme.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckan-wdi-theme for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/hbarrett/ckan-wdi-theme.git
    cd ckan-wdi-theme
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.wdi_theme --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckan-wdi-theme on PyPI
---------------------------------

ckan-wdi-theme should be availabe on PyPI as
https://pypi.python.org/pypi/ckan-wdi-theme. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckan-wdi-theme
----------------------------------------

ckan-wdi-theme is availabe on PyPI as https://pypi.python.org/pypi/ckan-wdi-theme.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
