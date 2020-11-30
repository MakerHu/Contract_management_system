from django.http import HttpResponse
from django.shortcuts import render
from CMSapp.models import user
from django.http import JsonResponse

# Create your views here.

def view_login(request):
    return render(request,'CMSapp/login.html')

def view_register(request):
    return render(request,'CMSapp/register.html')

def ajax_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(request)
    print(username)
    response = {}

    exists_username = user.objects.filter(username = username)
    print(exists_username)
    right_password = user.objects.filter(password = password)

    if exists_username:
        response['exists_username'] = 'success'
        if right_password:
            response['right_password'] = 'success'
        else:
            response['right_password'] = 'fail'
    else:
        response['exists_username'] = 'fail'

    return JsonResponse(response)
