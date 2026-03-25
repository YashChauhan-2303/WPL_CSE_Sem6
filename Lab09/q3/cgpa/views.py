from django.shortcuts import redirect, render

from .forms import CgpaForm


def input_view(request):
	if request.method == 'POST':
		form = CgpaForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			total_marks = form.cleaned_data['total_marks']
			cgpa = round(total_marks / 50, 2)

			request.session['name'] = name
			request.session['total_marks'] = total_marks
			request.session['cgpa'] = cgpa
			return redirect('result')
	else:
		form = CgpaForm()

	return render(request, 'cgpa/input.html', {'form': form})


def result_view(request):
	name = request.session.get('name')
	total_marks = request.session.get('total_marks')
	cgpa = request.session.get('cgpa')

	if name is None or total_marks is None or cgpa is None:
		return redirect('input')

	return render(
		request,
		'cgpa/result.html',
		{'name': name, 'total_marks': total_marks, 'cgpa': cgpa},
	)
