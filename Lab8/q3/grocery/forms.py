from django import forms

GROCERY_CHOICES = [
    ('Wheat', 'Wheat'),
    ('Jaggery', 'Jaggery'),
    ('Dal', 'Dal'),
    ('Rice', 'Rice'),
    ('Sugar', 'Sugar'),
]

class GroceryForm(forms.Form):
    items = forms.MultipleChoiceField(
        choices=GROCERY_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
