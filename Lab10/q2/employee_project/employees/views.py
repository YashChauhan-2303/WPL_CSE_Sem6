from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Works, Lives
from .forms import WorksForm, LivesForm, CompanySearchForm


def index(request):
    """Dashboard view"""
    works_count = Works.objects.count()
    lives_count = Lives.objects.count()
    companies = Works.objects.values_list('company_name', flat=True).distinct().count()
    
    context = {
        'works_count': works_count,
        'lives_count': lives_count,
        'companies': companies,
    }
    return render(request, 'employees/index.html', context)


def insert_works(request):
    """Insert data into WORKS table"""
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                f'Employee "{form.cleaned_data["person_name"]}" added to {form.cleaned_data["company_name"]}!'
            )
            return redirect('insert_works')
    else:
        form = WorksForm()
    
    works_list = Works.objects.all().order_by('-created_at')[:10]
    
    context = {
        'form': form,
        'recent_works': works_list,
    }
    return render(request, 'employees/insert_works.html', context)


def insert_lives(request):
    """Insert data into LIVES table"""
    if request.method == 'POST':
        form = LivesForm(request.POST)
        if form.is_valid():
            form.save()
            works = form.cleaned_data['works']
            messages.success(
                request, 
                f'Location for "{works.person_name}" ({works.company_name}) added!'
            )
            return redirect('insert_lives')
    else:
        form = LivesForm()
    
    lives_list = Lives.objects.select_related('works').order_by('-created_at')[:10]
    
    context = {
        'form': form,
        'recent_lives': lives_list,
    }
    return render(request, 'employees/insert_lives.html', context)


def search_company(request):
    """Search employees by company and display their cities"""
    results = None
    search_query = None
    form = CompanySearchForm()
    
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['company_name']
            
            # Get all employees from the company
            works_records = Works.objects.filter(
                company_name__icontains=search_query
            ).order_by('person_name')
            
            # For each employee, check if they have a location record
            results = []
            for work in works_records:
                # Use the one-to-one relationship
                try:
                    location = work.location
                    results.append({
                        'person_name': work.person_name,
                        'company_name': work.company_name,
                        'salary': work.salary,
                        'city': location.city,
                        'street': location.street,
                    })
                except Lives.DoesNotExist:
                    # If no location info, still include the employee
                    results.append({
                        'person_name': work.person_name,
                        'company_name': work.company_name,
                        'salary': work.salary,
                        'city': 'Not available',
                        'street': 'Not available',
                    })
            
            if not results:
                messages.warning(request, f'No employees found for "{search_query}"')
    
    context = {
        'form': form,
        'results': results,
        'search_query': search_query,
    }
    return render(request, 'employees/search_company.html', context)


def view_all_works(request):
    """View all WORKS records"""
    works_list = Works.objects.all().order_by('-created_at')
    
    context = {
        'works_list': works_list,
    }
    return render(request, 'employees/view_all_works.html', context)


def view_all_lives(request):
    """View all LIVES records"""
    lives_list = Lives.objects.select_related('works').order_by('-created_at')
    
    context = {
        'lives_list': lives_list,
    }
    return render(request, 'employees/view_all_lives.html', context)
