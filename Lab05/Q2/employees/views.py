from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import json

from .models import Employee


def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})


@csrf_exempt
def check_eligibility(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    doj_str = data.get('date_of_joining', '')
    
    if not doj_str:
        return JsonResponse({'eligible': False, 'message': 'Date of joining required'})

    try:
        # Parse date in YYYY-MM-DD format
        doj = date.fromisoformat(doj_str)
    except ValueError:
        return JsonResponse({'eligible': False, 'message': 'Invalid date format'})

    today = date.today()
    years = (today - doj).days / 365.25

    if years > 5:
        return JsonResponse({'eligible': True, 'message': 'YES', 'years': round(years, 1)})
    else:
        return JsonResponse({'eligible': False, 'message': 'NO', 'years': round(years, 1)})
