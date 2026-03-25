from django.shortcuts import render
from .forms import GroceryForm

# Grocery items with prices
GROCERY_PRICES = {
    'Wheat': 40,
    'Jaggery': 60,
    'Dal': 80,
    'Rice': 50,
    'Sugar': 45,
}

def grocery_list(request):
    selected_items = []
    
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data['items']
            for item in items:
                selected_items.append({
                    'name': item,
                    'price': GROCERY_PRICES[item]
                })
    else:
        form = GroceryForm()
    
    context = {
        'form': form,
        'selected_items': selected_items,
    }
    return render(request, 'grocery/checklist.html', context)
