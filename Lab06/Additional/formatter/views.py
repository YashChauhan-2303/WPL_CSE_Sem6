from django.shortcuts import render


def index(request):
    context = {
        'name': '',
        'message': '',
        'bold': False,
        'italic': False,
        'underline': False,
        'color': 'red',
        'show_result': False,
    }
    
    if request.method == 'POST':
        action = request.POST.get('action', '')
        
        if action == 'display':
            context = {
                'name': request.POST.get('name', ''),
                'message': request.POST.get('message', ''),
                'bold': 'bold' in request.POST,
                'italic': 'italic' in request.POST,
                'underline': 'underline' in request.POST,
                'color': request.POST.get('color', 'red'),
                'show_result': True,
            }
        elif action == 'clear':
            # Reset to default values
            context = {
                'name': '',
                'message': '',
                'bold': False,
                'italic': False,
                'underline': False,
                'color': 'red',
                'show_result': False,
            }
    
    return render(request, 'formatter/index.html', context)
