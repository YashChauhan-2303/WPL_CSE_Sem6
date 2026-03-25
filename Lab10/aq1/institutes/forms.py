from django import forms
from .models import Institute


class InstituteSelectionForm(forms.Form):
    """Form to display institutes as a selectable list"""
    institute = forms.ModelChoiceField(
        queryset=Institute.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'institute-select'
        }),
        label='Select Institute',
        empty_label='-- Choose an Institute --'
    )
