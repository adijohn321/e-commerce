
# forms.py
from django import forms
from .models import *
 

  
class AdsCampaignForm(forms.ModelForm):
 
    class Meta:
        model = AdsCampaign
        fields = [
            'ads_description',
            'ads_name',
            'ads_image',
        ]
     