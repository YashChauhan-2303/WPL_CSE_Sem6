from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import string
import json


def generate_captcha():
    """Generate a random 6-character captcha"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=6))


def index(request):
    """Render the captcha page with a new captcha"""
    captcha_text = generate_captcha()
    request.session['captcha'] = captcha_text
    request.session['attempts'] = 0
    return render(request, 'captcha/index.html', {'captcha': captcha_text})


@csrf_exempt
def verify(request):
    """Verify the captcha input"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        data = request.POST

    user_input = data.get('captcha_input', '').strip().upper()
    stored_captcha = request.session.get('captcha', '')
    attempts = request.session.get('attempts', 0)

    if attempts >= 3:
        return JsonResponse({
            'success': False,
            'message': 'Too many failed attempts. TextBox disabled.',
            'disabled': True,
            'attempts': attempts
        })

    if user_input == stored_captcha:
        # Reset on success
        new_captcha = generate_captcha()
        request.session['captcha'] = new_captcha
        request.session['attempts'] = 0
        return JsonResponse({
            'success': True,
            'message': 'Captcha matched successfully! ✓',
            'disabled': False,
            'attempts': 0,
            'new_captcha': new_captcha
        })
    else:
        attempts += 1
        request.session['attempts'] = attempts
        disabled = attempts >= 3
        
        if disabled:
            message = 'Too many failed attempts (3). TextBox is now disabled.'
        else:
            message = f'Captcha mismatch! Attempts remaining: {3 - attempts}'
        
        return JsonResponse({
            'success': False,
            'message': message,
            'disabled': disabled,
            'attempts': attempts
        })


@csrf_exempt
def refresh(request):
    """Generate a new captcha"""
    new_captcha = generate_captcha()
    request.session['captcha'] = new_captcha
    # Don't reset attempts on refresh
    return JsonResponse({
        'captcha': new_captcha,
        'attempts': request.session.get('attempts', 0)
    })
