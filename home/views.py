from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import json
from home.query import user_registration
from home.query import address
from home.query import admin_registration
from home.query import admin_address
from home.query import admin_login
from home.query import user_login
from home.query import corse_name
from home.query import university
from home.query import price
from home.query import scholarship
from home.query import certificate
from home.query import education_infor
from home.query import pull_all_user
from home.query import pull_all_course
from home.query import  pull_all_universities
from home.query import pull_all_application

# Create your views here.



@csrf_exempt
def API(request):
    if request.method == "POST":
        client_request = request.body
        client_data = json.loads(client_request) 
        
        if client_data['code'] == 100:
            responseString = admin_registration(client_data['data'])

        if client_data['code'] == 101:
            responseString = admin_address(client_data['data'])

        if client_data['code'] == 102:
            responseString = user_registration(client_data['data'])

        if client_data['code'] == 103:
            responseString = user_address(client_data['data'])

        if client_data['code'] == 104:
            responseString = admin_login(client_data['data'])

        if client_data['code'] == 105:
            responseString = user_login(client_data['data'])

        if client_data['code'] == 106:
            responseString = corse_name(client_data['data'])

        if client_data['code'] == 107:
            responseString = university(client_data['data'])

        if client_data['code'] == 108:
            responseString = price(client_data['data'])

        if client_data['code'] == 109:
            responseString = scholarship(client_data['data'])

        if client_data['code'] == 110:
            responseString = certificate(client_data['data'])

        if client_data['code']  == 111:
            responseString = education_infor(client_data['data'])

        if client_data['code'] == 112:
            responseString  = pull_all_user(client_data['data'])

        if client_data['code'] == 113:
            responseString =  pull_all_universities(client_data['data'])

        if client_data['code'] == 114:
            responseString = pull_all_application(client_data['data'])

        if client_data['code'] == 115:
            responseString = pull_all_course(client_data['data'])                                                            
    
    return HttpResponse(responseString)  