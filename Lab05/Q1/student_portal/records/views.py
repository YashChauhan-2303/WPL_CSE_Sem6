from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
import json

from .models import StudentRecord


def index(request):
	records = StudentRecord.objects.order_by('-created_at')[:100]
	# pass serializable list to template
	records_list = list(records.values('id', 'name', 'dob', 'address', 'contact', 'email', 'maths', 'physics', 'chemistry', 'created_at'))
	return render(request, 'records/index.html', {'records_list': records_list})


@csrf_exempt
def submit_data(request):
	if request.method != 'POST':
		return JsonResponse({'ok': False, 'error': 'POST required'}, status=400)

	# accept JSON or form-encoded
	try:
		payload = json.loads(request.body.decode('utf-8')) if request.body else request.POST
	except Exception:
		payload = request.POST

	name = payload.get('name')
	dob = payload.get('dob')
	address = payload.get('address')
	contact = payload.get('contact')
	email = payload.get('email')
	try:
		maths = int(payload.get('maths') or 0)
		physics = int(payload.get('physics') or 0)
		chemistry = int(payload.get('chemistry') or 0)
	except ValueError:
		return JsonResponse({'ok': False, 'error': 'Marks must be integers'}, status=400)

	if isinstance(dob, str):
		dob = parse_date(dob)

	rec = StudentRecord.objects.create(
		name=name or '',
		dob=dob or None,
		address=address or '',
		contact=contact or '',
		email=email or '',
		maths=maths,
		physics=physics,
		chemistry=chemistry,
	)

	return JsonResponse({'ok': True, 'id': rec.id, 'percentage': rec.percentage(), 'total': rec.total()})
