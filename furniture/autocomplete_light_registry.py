import autocomplete_light
from models import salestax

	
autocomplete_light.register(salestax, autocomplete_js_attributes={
'placeholder': '(enter city)',
    },search_fields=['city',])