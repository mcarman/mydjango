# apps.snippets.urls
from django.conf.urls import patterns, url
from apps.snippets.models import Snippet
from apps.snippets.views import snippet_list, snippet_detail


urlpatterns = patterns('apps.snippets.views',
   url(r'^snippets/$', 'snippet_list'),

    # list the details of selected snippet
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)
