from django import forms
from .models import Human


class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['first_name', 'last_name', 'phone', 'address', 'city']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'phone': forms.TextInput(),
            'address': forms.TextInput(),
            'city': forms.TextInput(),
        }
