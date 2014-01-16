import autocomplete_light
from models import salestax, item, vendor

	
autocomplete_light.register(salestax, autocomplete_js_attributes={
'placeholder': '(enter city)',
    }
	,search_fields=['city',],
	)

vendors = vendor.objects.all()

for vendor in vendors:

	autocomplete_light.register(item, name=str(vendor.name.replace(" ", "")), 
							choices=item.objects.filter(vendor_id=vendor.id),
							autocomplete_js_attributes={
														'placeholder': '(enter sku)',
							},search_fields=['sku',])


