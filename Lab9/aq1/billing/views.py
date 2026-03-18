from django.shortcuts import redirect, render

from .forms import BillForm


PRICE_TABLE = {
	'HP': {'Mobile': 15000, 'Laptop': 55000},
	'Nokia': {'Mobile': 12000, 'Laptop': 40000},
	'Samsung': {'Mobile': 18000, 'Laptop': 65000},
	'Motorola': {'Mobile': 14000, 'Laptop': 50000},
	'Apple': {'Mobile': 60000, 'Laptop': 120000},
}


def order_view(request):
	if request.method == 'POST':
		form = BillForm(request.POST)
		if form.is_valid():
			brand = form.cleaned_data['brand']
			items = form.cleaned_data['items']
			quantities = {
				'Mobile': form.cleaned_data['mobile_quantity'],
				'Laptop': form.cleaned_data['laptop_quantity'],
			}

			line_items = []
			total_amount = 0
			for item in items:
				unit_price = PRICE_TABLE[brand][item]
				quantity = quantities[item]
				amount = unit_price * quantity
				total_amount += amount
				line_items.append(
					{
						'item': item,
						'unit_price': unit_price,
						'quantity': quantity,
						'amount': amount,
					}
				)

			request.session['brand'] = brand
			request.session['line_items'] = line_items
			request.session['total_amount'] = total_amount
			return redirect('bill')
	else:
		form = BillForm()

	return render(request, 'billing/order.html', {'form': form})


def bill_view(request):
	brand = request.session.get('brand')
	line_items = request.session.get('line_items')
	total_amount = request.session.get('total_amount')

	if brand is None or line_items is None or total_amount is None:
		return redirect('order')

	context = {
		'brand': brand,
		'line_items': line_items,
		'total_amount': total_amount,
	}
	return render(request, 'billing/bill.html', context)
