
from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^$', view.account),
    url(r'^show$', view.show),
]
