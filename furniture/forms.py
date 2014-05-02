from django import forms

import autocomplete_light_registry
import autocomplete_light

from models import salestax

class taxForm(forms.Form):
    city = forms.CharField(
        widget=autocomplete_light.TextWidget('salestaxAutocomplete'))

class ABCFurnitureChairsForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("ABCFurnitureChairs"))

class ABCFurnitureDesksForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("ABCFurnitureDesks"))
		
class XYZElectronicsForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("XYZElectronics"))
		
class MNOChairsForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("MNOChairs"))
		

