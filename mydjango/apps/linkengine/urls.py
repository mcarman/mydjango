# apps.links.urls
from django.conf.urls import patterns, url
from views import LinkListView


urlpatterns = patterns('',
    url(r'^$', LinkListView.as_view(), name='links'))
