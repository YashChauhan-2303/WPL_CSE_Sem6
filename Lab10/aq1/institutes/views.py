from django.shortcuts import render
from .models import Institute
from .forms import InstituteSelectionForm


def institute_list(request):
    """Display institutes in a list box (select dropdown)"""
    institutes = Institute.objects.all().order_by('name')
    form = InstituteSelectionForm()
    
    selected_institute = None
    if request.method == 'POST':
        form = InstituteSelectionForm(request.POST)
        if form.is_valid():
            selected_institute = form.cleaned_data['institute']
    
    context = {
        'form': form,
        'institutes': institutes,
        'selected_institute': selected_institute,
        'total_institutes': institutes.count(),
    }
    return render(request, 'institutes/institute_list.html', context)
