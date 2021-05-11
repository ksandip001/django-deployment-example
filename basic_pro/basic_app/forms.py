from django import forms
from basic_app.models import Bjp


class FormName(forms.ModelForm):
    class Meta:
        model = Bjp
        fields= '__all__'
        
