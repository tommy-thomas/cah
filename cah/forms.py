from django import forms
from cah.models import CAHModel
from django_google_maps.widgets import GoogleMapsAddressWidget


class CAHForm(forms.ModelForm):

    class Meta(object):
        model = CAHModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }