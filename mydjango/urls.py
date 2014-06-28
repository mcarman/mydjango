from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/
#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Blog URLs
    url(r'', include('apps.blogengine.urls')),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
