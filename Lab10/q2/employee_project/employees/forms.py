from django import forms
from .models import Works, Lives


class WorksForm(forms.ModelForm):
    """Form for inserting data into WORKS table"""
    
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']
        widgets = {
            'person_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter person name',
                'required': True
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name',
                'required': True
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary (e.g., 50000.00)',
                'step': '0.01',
                'min': '0'
            }),
        }


class LivesForm(forms.ModelForm):
    """Form for inserting data into LIVES table"""
    
    class Meta:
        model = Lives
        fields = ['works', 'street', 'city']
        widgets = {
            'works': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter street address',
                'required': True
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city name',
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show employee name and company in the dropdown
        self.fields['works'].queryset = Works.objects.select_related().order_by('person_name')
        self.fields['works'].label_from_instance = lambda obj: f"{obj.person_name} at {obj.company_name} (${obj.salary})"


class CompanySearchForm(forms.Form):
    """Form for searching employees by company"""
    company_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter company name to search',
            'required': True
        })
    )
