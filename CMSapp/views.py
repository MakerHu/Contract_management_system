from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def view_login(request):
    return render(request,'CMSapp/login.html');