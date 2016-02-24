from django.conf.urls import patterns, include, url
from django.contrib import admin

from edziennik.views import index

urlpatterns = [
    url(r'^$', index),

    url(r'^admin/', admin.site.urls),
]
