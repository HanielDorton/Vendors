from django.conf.urls import patterns, include, url
from django.conf import settings 
from django.conf.urls.defaults import *
from vendors import settings
import autocomplete_light
autocomplete_light.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	# Index #
    (r'^$','furniture.views.index'),
	(r'^home/$', 'furniture.views.index'),
	# Login / Log out #
	(r'^login/$', 'django.contrib.auth.views.login',),	
	(r'^logout/$', 'furniture.views.logout_view'),
	# List of Vendors to choose from #
	(r'^([a-zA-z_]+)/$', 'furniture.views.vendors_list'),
	# Vendor Information Page #
	(r'^([a-zA-z_]+)/([0-9]|[1-9][0-9])/$', 'furniture.views.vendor_info'),
	# Item Lookup Page #
	(r'^([a-zA-z_]+)/([0-9]|[1-9][0-9])/search/$', 'furniture.views.item_search'),


	
	
	
	(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 url(r'^autocomplete/', include('autocomplete_light.urls')),
	 
	 
)

