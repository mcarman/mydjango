# apps.snippets.urls
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views


urlpatterns = format_suffix_patterns(patterns('snippets.views',
    # list of snippets page
    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),

    # details of a snippet page
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),

    # the highlighted view of the snippet page
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),

    # list of users page
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),

    # single user detail page
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))
