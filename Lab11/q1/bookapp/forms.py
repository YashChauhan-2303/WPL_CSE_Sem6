from django import forms
from .models import Author, Publisher, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'street_address', 'city', 'state_province', 'country', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'street_address': forms.TextInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input'}),
            'state_province': forms.TextInput(attrs={'class': 'form-input'}),
            'country': forms.TextInput(attrs={'class': 'form-input'}),
            'website': forms.URLInput(attrs={'class': 'form-input'}),
        }


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'authors', 'publisher']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'publication_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'publisher': forms.Select(attrs={'class': 'form-input'}),
        }
