from django.db.models.fields import json
from django.shortcuts import render, HttpResponse
from .models import User, SelfAssessment
import json
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
# Create your views here.
def home_page(request):
    return render(request, 'home.html', context={})

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        user_info=json.loads(request.body.decode('utf-8'))
        print(json.loads(request.body.decode('utf-8')))
        user=User.objects.create(name=user_info['name'],
                                mobile_number=user_info['phoneNumber'],
                                pin_code=user_info['pinCode'])
        user.save()

    return HttpResponse(json.dumps({'userId': user.id}))


@csrf_exempt
def self_assessment_view(request):
    if request.method == 'POST':
        self_assessment=json.loads(request.body.decode('utf-8'))
        print(json.loads(request.body.decode('utf-8')))
        assessment=SelfAssessment.objects.create(User=User.objects.get(id=int(self_assessment['userId'])), 
                                                                symptoms=str(self_assessment['symptoms']), 
                                                                travel_history=bool(self_assessment['travelHistory']),
                                                                covid_contact=bool(self_assessment['contactWithCovidPatient']))
        assessment.save()
        risk_percent=0
        if len(self_assessment['symptoms']) == 0 and not bool(self_assessment['travelHistory']) and not bool(self_assessment['contactWithCovidPatient']):
            risk_percent=5
        elif len(self_assessment['symptoms']) == 1:
            if bool(self_assessment['contactWithCovidPatient']) or bool(self_assessment['travelHistory']):
                risk_percent=50
        elif len(self_assessment['symptoms']) == 2:
            if bool(self_assessment['contactWithCovidPatient']) or bool(self_assessment['travelHistory']):
                risk_percent=75
        elif len(self_assessment['symptoms']) > 2:
            if bool(self_assessment['contactWithCovidPatient']) or bool(self_assessment['travelHistory']):
                risk_percent=95
    return HttpResponse(json.dumps({'riskPercentage': risk_percent}))

@csrf_exempt
def health_worker_register(request):
    if request.method == 'POST':
        user_info=json.loads(request.body.decode('utf-8'))
        print(json.loads(request.body.decode('utf-8')))
        user=User.objects.create(name=user_info['name'], mobile_number=user_info['phoneNumber'], pin_code=user_info['pinCode'], is_admin=True)
        user.save()
    return HttpResponse(json.dumps({'adminId': user.id}))

@csrf_exempt
def update_covid_result(request):
    if request.method == 'POST':
        import pdb;pdb.set_trace()
        result_info=json.loads(request.body.decode('utf-8'))
        print(json.loads(request.body.decode('utf-8')))
        user=User.objects.get(id=result_info['usedId'])
        user.covid_status = result_info['result']
        user.save()
    return HttpResponse(json.dumps({'updated': True}))