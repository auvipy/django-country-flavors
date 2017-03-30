=====
Usage
=====

To use django-country-flavors in a project, add it to your `INSTALLED_APPS`:

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
