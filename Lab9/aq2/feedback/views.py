from django.shortcuts import render

from .forms import FeedbackForm


def feedback_form_view(request):
	success_message = ''

	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			gender = form.cleaned_data['gender']
			course = form.cleaned_data['course']
			technical_coverage = form.cleaned_data['technical_coverage']
			success_message = (
				f'Thank you {name} ({gender}). Your feedback for {course} '
				f'with technical coverage rated as {technical_coverage} has been submitted successfully.'
			)
			form = FeedbackForm()
	else:
		form = FeedbackForm()

	return render(
		request,
		'feedback/feedback_form.html',
		{'form': form, 'success_message': success_message},
	)
