from django.conf.urls import patterns, include, url

import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	
    (r'^$','furniture.views.index'),
    (r'^home/$', 'furniture.views.index'),
	(r'^login/$', 'django.contrib.auth.views.login',),	
	(r'^logout/$', 'furniture.views.logout_view'),
	(r'^MFC_view/$', 'furniture.views.mfc_view'),
	(r'^customer_view/$', 'furniture.views.customer_view'),
	(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 
	 url(r'^autocomplete/', include('autocomplete_light.urls')),
	 
	 
)

