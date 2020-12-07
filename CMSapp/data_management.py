import os
import django
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from CMSapp import models
import json


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()


def data_draft_contract(request):
    pass

def data_allocation(request):
    if request.session.get('is_login', None):
        allocation_conid = request.POST.get('keyword')
        response = {}
        username = models.role.objects.exclude(rolename='newuser')
        response['username'] = username

        processConidEntity = models.contract_process.objects.filter(conid=allocation_conid)
        countersign = models.contract_process.objects.filter(conid=processConidEntity, type=1)
        approve = models.contract_process.objects.filter(conid=processConidEntity, type=2)
        sign = models.contract_process.objects.filter(conid=processConidEntity, type=3)

        response['countersign'] = countersign
        response['approve'] = approve
        response['sign'] = sign
        return render(request, 'CMSapp/contract_allocation.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')

def ajax_contract_allocation(request):
    data_countersign = request.POST.getlist('data_countersign')
    data_approve = request.POST.getlist('data_approve')
    data_sign = request.POST.getlist('data_sign')

    countersign = json.loads(data_countersign[0])
    approve = json.loads(data_approve[0])
    sign = json.loads(data_sign[0])


    response = {'is': 'success'}

    return JsonResponse(response)


def data_authorize(request):
    if request.session.get('is_login', None):
        authorized_username = request.POST.get('keyword')
        response = {}
        rolelist = models.role.objects.all()
        response['rolelist'] = rolelist
        response['authorized_username'] = authorized_username
        # 要修改的用户的角色
        authorized_rolename=models.right.objects.filter(username=authorized_username)[0].rolename.rolename
        response['authorized_rolename'] = authorized_rolename
        return render(request, 'CMSapp/authority_assignment.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


def data_updateAuthority(request):
    username = request.POST.get('username')
    new_rolename = request.POST.get('new_rolename')
    models.right.objects.filter(username=username).update(rolename=new_rolename)
    return HttpResponse(request)
