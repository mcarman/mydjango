# apps.REST.urls
from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns(patterns('',
    # REST API entry page  
    url(r'^$', 'api_root'),

    # endpoint for the api base view
    url(r'^api-auth/',
        namespace='REST')
))
