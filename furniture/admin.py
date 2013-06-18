from django.contrib import admin
from furniture.models import vendor, item, salestax

admin.site.register(vendor)
admin.site.register(item)
admin.site.register(salestax)