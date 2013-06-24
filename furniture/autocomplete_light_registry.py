import autocomplete_light
from models import salestax

class taxautocomplete(autocomplete_light.AutocompleteModelBase):
	search_fields = ['^city',]
	
autocomplete_light.register(salestax, taxautocomplete)