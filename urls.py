from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),

    # Examples:
    # url(r'^$', 'lespecial.views.home', name='home'),
    # url(r'^lespecial/', include('lespecial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^grappelli/', include('grappelli.urls')),
    (r'^contact/', include('contact_form.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^shows/', include('agenda.urls')),
    (r'^$', direct_to_template, {'template': 'base.html'}),


    (r'^merchandise/', include('lfs.core.urls')),
    (r'^merchandise/manage/', include('lfs.manage.urls')),
    (r'^merchandise/reviews/', include('reviews.urls')),
    (r'^merchandise/paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^merchandise/paypal/pdt/', include('paypal.standard.pdt.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
)

if settings.DEBUG:
   urlpatterns += patterns('',
      url(r'', include('debug_toolbar_user_panel.urls')),
   )
