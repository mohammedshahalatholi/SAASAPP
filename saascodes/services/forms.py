from django import forms
from . models import Services

class servicefrm(forms.ModelForm):
    class Meta:
        model=Services
        fields=['Title','Link','Discription']