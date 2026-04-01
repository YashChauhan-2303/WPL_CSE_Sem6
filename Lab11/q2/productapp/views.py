from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


@require_http_methods(["GET", "POST"])
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})
