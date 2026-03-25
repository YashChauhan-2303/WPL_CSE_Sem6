from django import forms


class BillForm(forms.Form):
    brand = forms.ChoiceField(
        label='Brand',
        choices=[
            ('HP', 'HP'),
            ('Nokia', 'Nokia'),
            ('Samsung', 'Samsung'),
            ('Motorola', 'Motorola'),
            ('Apple', 'Apple'),
        ],
        widget=forms.RadioSelect,
    )
    items = forms.MultipleChoiceField(
        label='Items',
        choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop')],
        widget=forms.CheckboxSelectMultiple,
    )
    mobile_quantity = forms.IntegerField(
        label='Mobile Quantity',
        min_value=0,
        required=False,
        initial=0,
    )
    laptop_quantity = forms.IntegerField(
        label='Laptop Quantity',
        min_value=0,
        required=False,
        initial=0,
    )

    def clean(self):
        cleaned_data = super().clean()
        items = cleaned_data.get('items', [])
        mobile_quantity = cleaned_data.get('mobile_quantity') or 0
        laptop_quantity = cleaned_data.get('laptop_quantity') or 0

        if not items:
            raise forms.ValidationError('Please select at least one item.')

        if 'Mobile' in items and mobile_quantity < 1:
            self.add_error('mobile_quantity', 'Enter Mobile quantity for selected item.')

        if 'Laptop' in items and laptop_quantity < 1:
            self.add_error('laptop_quantity', 'Enter Laptop quantity for selected item.')

        return cleaned_data
