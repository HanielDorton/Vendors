from django import forms

import autocomplete_light_registry
import autocomplete_light

from models import salestax

class taxForm(forms.Form):
    city = forms.CharField(
        widget=autocomplete_light.TextWidget('salestaxAutocomplete'))
		
class skuForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget('itemAutocomplete'))
		