from django import forms


class CgpaForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    total_marks = forms.FloatField(label='Total Marks', min_value=0)
