from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .libs.talkdb import Talkdb_operation
import json
# Create your views here.


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

def get_sql():
    print(Talkdb_operation().get_all_data())

# Create your views here.
def show_talk_info(request):

    ##getting tainan weather
    all_talk = Talkdb_operation().get_all_data()

    return render(request, 'experiment/Teacher_monitor.html' , {
        'test': all_talk
    })