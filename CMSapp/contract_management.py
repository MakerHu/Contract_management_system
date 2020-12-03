from django.http import HttpResponse
from django.shortcuts import render
from CMSapp.models import user
from django.http import JsonResponse
from django.shortcuts import redirect

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")# project_name 项目名称
django.setup()



