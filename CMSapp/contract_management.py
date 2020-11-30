from django.http import HttpResponse
from django.shortcuts import render
from CMSapp.models import user
from django.http import JsonResponse

def index(request):
    return render(request,'CMSapp/index.html')