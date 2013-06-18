from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','furniture.views.index'),
    (r'^home/$', 'furniture.views.index'),
	(r'^login/$', 'furniture.views.login'), 
	(r'^logout/$', 'furniture.views.logout'),
	(r'^success/$', 'furniture.views.success'),	
	(r'^failedlogin/$', 'furniture.views.failedlogin'),	

	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'furniture/login.html'}),	
	
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
