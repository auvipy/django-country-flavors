# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from countryflavors.urls import urlpatterns as countryflavors_urls

urlpatterns = [
    url(r'^', include(countryflavors_urls, namespace='countryflavors')),
]
