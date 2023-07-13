from django import forms
from app.models import *

class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
