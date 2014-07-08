# apps.linkengine.urls
from django.conf.urls import patterns, url
from django.contrib.auth.models import User
from apps.linkengine.views import LinkListView, LinkCreateView, LinkUpdateView
from apps.linkengine.views import LinkDetailView, LinkDeleteView


urlpatterns = patterns('',
    # list of links, paginated
    url(r'^linklist/$', LinkListView.as_view(), name='links'),

    # create a link
    url(r'^create/$', (LinkCreateView.as_view()),
        name='link_create'),

    # detail link page
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(),
        name='link_detail'),

    # edit and update the link (auth)
    url(r'^link/update/(?P<pk>\d+)/$', (LinkUpdateView.as_view()),
        name='link_update'),

    # delete the link (auth)
    url(r'^link/delete/(?P<pk>\d+)/$', (LinkDeleteView.as_view()),
        name='link_delete'),
)
