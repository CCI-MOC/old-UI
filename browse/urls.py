from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from browse.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
)
