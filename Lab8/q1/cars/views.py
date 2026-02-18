from django.shortcuts import render, redirect
from urllib.parse import urlencode
from .forms import CarSelectionForm

def select_car(request):
    """View to display the car selection form"""
    if request.method == 'POST':
        form = CarSelectionForm(request.POST)
        if form.is_valid():
            params = {
                'customer_name': form.cleaned_data['customer_name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'manufacturer': form.cleaned_data['manufacturer'],
                'model': form.cleaned_data['model'],
                'year': form.cleaned_data['year'],
                'color': form.cleaned_data['color'],
                'body_type': form.cleaned_data['body_type'],
                'fuel_type': form.cleaned_data['fuel_type'],
                'transmission': form.cleaned_data['transmission'],
                'budget': form.cleaned_data['budget'],
                'comments': form.cleaned_data['comments'],
            }
            return redirect(f'/display/?{urlencode(params)}')
    else:
        form = CarSelectionForm()
    
    context = {
        'form': form
    }
    return render(request, 'cars/select_car.html', context)

def display_car(request):
    """View to display the selected car details"""
    context = {
        'customer_name': request.GET.get('customer_name', ''),
        'email': request.GET.get('email', ''),
        'phone': request.GET.get('phone', ''),
        'manufacturer': request.GET.get('manufacturer', ''),
        'model': request.GET.get('model', ''),
        'year': request.GET.get('year', ''),
        'color': request.GET.get('color', ''),
        'body_type': request.GET.get('body_type', ''),
        'fuel_type': request.GET.get('fuel_type', ''),
        'transmission': request.GET.get('transmission', ''),
        'budget': request.GET.get('budget', ''),
        'comments': request.GET.get('comments', ''),
    }
    return render(request, 'cars/display_car.html', context)
