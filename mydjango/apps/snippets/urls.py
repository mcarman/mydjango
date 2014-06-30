# apps.snippets.urls
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('apps.snippets.views',
   url(r'^snippets/$', 'snippet_list'),

    # list the details of selected snippet
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
