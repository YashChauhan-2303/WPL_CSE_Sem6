from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Human
from .forms import HumanForm


def index(request):
    humans = Human.objects.all()
    selected_human = None
    form = HumanForm()
    add_form = HumanForm()
    
    if 'human_id' in request.GET:
        try:
            selected_human = Human.objects.get(id=request.GET['human_id'])
            form = HumanForm(instance=selected_human)
        except Human.DoesNotExist:
            pass
    
    context = {
        'humans': humans,
        'selected_human': selected_human,
        'form': form,
        'add_form': add_form,
    }
    return render(request, 'index.html', context)


@require_http_methods(["POST"])
def update_human(request):
    human_id = request.POST.get('human_id')
    
    if not human_id:
        return redirect('index')
    
    try:
        human = Human.objects.get(id=human_id)
        form = HumanForm(request.POST, instance=human)
        if form.is_valid():
            form.save()
    except Human.DoesNotExist:
        pass
    
    return redirect('index')


@require_http_methods(["POST"])
def delete_human(request):
    human_id = request.POST.get('human_id')
    
    if human_id:
        try:
            human = Human.objects.get(id=human_id)
            human.delete()
        except Human.DoesNotExist:
            pass
    
    return redirect('index')


@require_http_methods(["POST"])
def add_human(request):
    form = HumanForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')
