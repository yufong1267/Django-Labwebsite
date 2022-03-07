from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .libs.talkdb import Talkdb_operation
import json



import sys
sys.path.append("..")
from libs.weather import Get_Weather

# Create your views here.
def show_member_info(request):

    ##getting tainan weather
    result = Get_Weather().get_weather('tainan')

    return render(request, 'lab_member/member_page.html' , {
        'member_name': result,
        'member_age': '23'
    })

def receive_post(request):
    if(request.method == 'POST'):
        reg = request.body.decode()

        #reg = Talkdb_operation().talkdb_insert('777' , 'request.body' , '12')
        print(type(reg))
        reg = json.loads(reg)

        print(type(reg) , reg)


        return HttpResponse("OK")
    
    
    reg = request.method
    return JsonResponse({'foo':reg})