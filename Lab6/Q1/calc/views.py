from django.shortcuts import render


def calculator(request):
    result = None
    error = None
    num1 = ''
    num2 = ''
    operation = 'add'
    
    if request.method == 'POST':
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        operation = request.POST.get('operation', 'add')
        
        try:
            n1 = int(num1)
            n2 = int(num2)
            
            if operation == 'add':
                result = n1 + n2
            elif operation == 'subtract':
                result = n1 - n2
            elif operation == 'multiply':
                result = n1 * n2
            elif operation == 'divide':
                if n2 == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = n1 / n2
        except ValueError:
            error = "Please enter valid integers!"
    
    context = {
        'result': result,
        'error': error,
        'num1': num1,
        'num2': num2,
        'operation': operation,
    }
    return render(request, 'calc/index.html', context)
