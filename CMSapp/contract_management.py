from django.http import HttpResponse
from django.shortcuts import render
from CMSapp.models import user
from django.http import JsonResponse
from django.shortcuts import redirect

# def index(request):
#     return render(request,'CMSapp/index.html')

def index(request):
    if request.session.get('is_login', None):
        return render(request,'CMSapp/index.html')
    else:
        return redirect('/login/')
