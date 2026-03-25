from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
	form = RegisterForm(request.POST or None)
	return render(request, 'accounts/register.html', {'form': form})


def success_view(request):
	if request.method != 'POST':
		return redirect('register')

	form = RegisterForm(request.POST)
	if not form.is_valid():
		return render(request, 'accounts/register.html', {'form': form})

	context = {
		'username': form.cleaned_data['username'],
		'email': form.cleaned_data.get('email', ''),
		'contact_number': form.cleaned_data.get('contact_number', ''),
	}
	return render(request, 'accounts/success.html', context)
