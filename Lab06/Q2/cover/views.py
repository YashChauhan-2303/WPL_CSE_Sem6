from django.shortcuts import render


def magazine_cover(request):
    context = {
        'title': '',
        'subtitle': '',
        'headline1': '',
        'headline2': '',
        'headline3': '',
        'bg_color': '#1a1a2e',
        'title_color': '#ffffff',
        'subtitle_color': '#e94560',
        'headline_color': '#ffffff',
        'title_size': '48',
        'subtitle_size': '24',
        'headline_size': '18',
        'image_choice': 'fashion',
        'show_preview': False,
    }
    
    if request.method == 'POST':
        context = {
            'title': request.POST.get('title', 'MAGAZINE'),
            'subtitle': request.POST.get('subtitle', ''),
            'headline1': request.POST.get('headline1', ''),
            'headline2': request.POST.get('headline2', ''),
            'headline3': request.POST.get('headline3', ''),
            'bg_color': request.POST.get('bg_color', '#1a1a2e'),
            'title_color': request.POST.get('title_color', '#ffffff'),
            'subtitle_color': request.POST.get('subtitle_color', '#e94560'),
            'headline_color': request.POST.get('headline_color', '#ffffff'),
            'title_size': request.POST.get('title_size', '48'),
            'subtitle_size': request.POST.get('subtitle_size', '24'),
            'headline_size': request.POST.get('headline_size', '18'),
            'image_choice': request.POST.get('image_choice', 'fashion'),
            'show_preview': True,
        }
    
    return render(request, 'cover/index.html', context)
