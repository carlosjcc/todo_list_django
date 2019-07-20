from django import forms
from .models import List

class ListForm(forms.ModelForm):
    """docstring for ClassName"""
    class Meta:
        model = List
        fields = ["item", "completed"]
        