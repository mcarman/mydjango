# apps.snippets.urls
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views


urlpatterns = patterns('',
   # list of snippets
   url(r'^snippets/$', views.SnippetList.as_view()),

    # list the details of selected snippet
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

# accept suffixes to set content type
urlpatterns = format_suffix_patterns(urlpatterns)
