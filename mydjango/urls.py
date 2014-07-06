from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from apps.linkengine.views import UserProfileDetailView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Login template
    url(r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'registration/login.html'}, name="login"),

    # logout landing page
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
    name="logout"),

    # Accounts landing page
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),

    # Blog URLs
    url(r'', include('apps.blogengine.urls')),

    # Flat pages
    url(r'^flat/', include('django.contrib.flatpages.urls')),

    # Links pages
    url(r'', include('apps.linkengine.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
