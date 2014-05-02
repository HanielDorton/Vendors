from django import forms

import autocomplete_light_registry
import autocomplete_light

from models import salestax

class taxForm(forms.Form):
    city = forms.CharField(
        widget=autocomplete_light.TextWidget('salestaxAutocomplete'))

class USForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("ABCFurnitureChairs"))

class DMIFairplexForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("ABCFurnitureDesks"))
		
class CMAmberForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("XYZElectronics"))
		
class BossForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("MNOChairs"))
		

