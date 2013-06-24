import autocomplete_light
from models import salestax, item

	
autocomplete_light.register(salestax, autocomplete_js_attributes={
'placeholder': '(enter city)',
    },search_fields=['city',])
	
autocomplete_light.register(item, autocomplete_js_attributes={
'placeholder': '(enter sku)',
    },search_fields=['sku',])