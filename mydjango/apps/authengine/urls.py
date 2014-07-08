# apps.authengine.urls
from django.conf.urls import patterns, url
from django.contrib.auth import views


urlpatterns = patterns('',
    # login page 
    url(r'^login/$', 'login', {'template_name': 'authengine.login.html'},
        name='mydjango_login'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'authengine/login.html'}),

    # landing page for logout
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='mydjango_logout'),
)
