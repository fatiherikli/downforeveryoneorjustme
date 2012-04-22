from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'downforeveryoneorjustme.main.views.home', name='home'),
    url(r'^without-celery', 'downforeveryoneorjustme.main.views.check_direct', name='check_direct',  ),
    url(r'^with-celery$', 'djcelery.views.apply', {'task_name':'web_site_status'}, name='check',  ),
    url(r'^status/(.+)$', 'djcelery.views.task_status', name='status',  ),
    # url(r'^downforeveryoneorjustme/', include('downforeveryoneorjustme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)

