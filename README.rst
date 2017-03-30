=============================
django-country-flavors
=============================

.. image:: https://badge.fury.io/py/countryflavors.svg
    :target: https://badge.fury.io/py/countryflavors

.. image:: https://travis-ci.org/auvipy/countryflavors.svg?branch=master
    :target: https://travis-ci.org/auvipy/countryflavors

.. image:: https://codecov.io/gh/auvipy/countryflavors/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/auvipy/countryflavors

Better local flavors for countries

Documentation
-------------

The full documentation is at https://countryflavors.readthedocs.io.

Quickstart
----------

Install django-country-flavors::

    pip install countryflavors

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'countryflavors.apps.CountryflavorsConfig',
        ...
    )

Add django-country-flavors's URL patterns:

.. code-block:: python

    from countryflavors import urls as countryflavors_urls


    urlpatterns = [
        ...
        url(r'^', include(countryflavors_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
