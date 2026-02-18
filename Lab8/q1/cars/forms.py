from django import forms

CAR_MANUFACTURERS = [
    ('', '-- Select Manufacturer --'),
    ('Toyota', 'Toyota'),
    ('Honda', 'Honda'),
    ('Ford', 'Ford'),
    ('BMW', 'BMW'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Audi', 'Audi'),
    ('Volkswagen', 'Volkswagen'),
    ('Hyundai', 'Hyundai'),
    ('Nissan', 'Nissan'),
    ('Chevrolet', 'Chevrolet'),
]

YEAR_CHOICES = [('', '-- Select Year --')] + [(str(year), str(year)) for year in range(2024, 1999, -1)]

COLOR_CHOICES = [
    ('', '-- Select Color --'),
    ('White', 'White'),
    ('Black', 'Black'),
    ('Silver', 'Silver'),
    ('Gray', 'Gray'),
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Orange', 'Orange'),
    ('Brown', 'Brown'),
]

FUEL_TYPE_CHOICES = [
    ('', '-- Select Fuel Type --'),
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
    ('CNG', 'CNG'),
]

TRANSMISSION_CHOICES = [
    ('', '-- Select Transmission --'),
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('CVT', 'CVT'),
    ('Semi-Automatic', 'Semi-Automatic'),
]

BODY_TYPE_CHOICES = [
    ('', '-- Select Body Type --'),
    ('Sedan', 'Sedan'),
    ('SUV', 'SUV'),
    ('Hatchback', 'Hatchback'),
    ('Coupe', 'Coupe'),
    ('Convertible', 'Convertible'),
    ('Wagon', 'Wagon'),
    ('Truck', 'Truck'),
]

class CarSelectionForm(forms.Form):
    # Customer Information
    customer_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'customer_name',
            'placeholder': 'Enter your full name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Enter your email address'
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone',
            'placeholder': 'Enter your phone number'
        })
    )
    
    # Car Information
    manufacturer = forms.ChoiceField(
        choices=CAR_MANUFACTURERS,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'manufacturer'
        })
    )
    model = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'model',
            'placeholder': 'Enter model name (e.g., Camry, Civic)'
        })
    )
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'year'
        })
    )
    color = forms.ChoiceField(
        choices=COLOR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'color'
        })
    )
    body_type = forms.ChoiceField(
        choices=BODY_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'body_type'
        })
    )
    fuel_type = forms.ChoiceField(
        choices=FUEL_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'fuel_type'
        })
    )
    transmission = forms.ChoiceField(
        choices=TRANSMISSION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'transmission'
        })
    )
    budget = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'budget',
            'placeholder': 'Enter your budget (e.g., $25,000)'
        })
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'comments',
            'placeholder': 'Any additional requirements or comments...',
            'rows': 3
        })
    )

