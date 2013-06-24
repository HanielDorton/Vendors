from django import forms

import autocomplete_light

from models import salestax


class taxForm(forms.ModelForm):
    tax = forms.ModelChoiceField(salestax.objects.all(), label=_('city'), widget=autocomplete_light.ChoiceWidget('CityAutocomplete'))