import os
import django
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from CMSapp import models


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()


def data_draft_contract(request):
    pass


def test(request):
    countersign_person = request.POST.get('countersign_person')
    approve_person = request.POST.get('approve_person')
    sign_person = request.POST.get('sign_person')

    # print('000000000000000000000000000000000')
    #
    # print('countersign_person')
    # print(countersign_person)
    #
    # print('approve_person')
    # print(approve_person)
    #
    # print('sign_person')
    # print(sign_person)

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
