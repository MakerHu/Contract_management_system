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
        userrightlist = models.right.objects.exclude(rolename='newuser')
        response['userrightlist'] = userrightlist
        rolefunctionlist = models.role_function.objects.all()
        response['rolefunctionlist'] = rolefunctionlist
        contractname = models.contract.objects.filter(conid=allocation_conid)[0].conname

        response['conid'] = allocation_conid
        response['contractname'] = contractname

        processConidEntity = models.contract.objects.filter(conid=allocation_conid)[0]
        countersign = models.contract_process.objects.filter(conid=processConidEntity, type=1)
        approve = models.contract_process.objects.filter(conid=processConidEntity, type=2)
        sign = models.contract_process.objects.filter(conid=processConidEntity, type=3)

        response['countersign'] = countersign
        response['approve'] = approve
        response['sign'] = sign

        canCountersignRoles = models.role_function.objects.filter(function='contract_countersign')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left1_rightlist = models.right.objects.filter(rolename__rolename__in=canCountersignRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canApprovalRoles = models.role_function.objects.filter(function='contract_approval')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left2_rightlist = models.right.objects.filter(rolename__rolename__in=canApprovalRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canSignRoles = models.role_function.objects.filter(function='contract_sign')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left3_rightlist = models.right.objects.filter(rolename__rolename__in=canSignRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        response['left1_rightlist'] = left1_rightlist
        response['left2_rightlist'] = left2_rightlist
        response['left3_rightlist'] = left3_rightlist

        return render(request, 'CMSapp/contract_allocation.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


def data_updateAllocation(request):
    data_countersign = request.POST.getlist('data_countersign')
    data_approve = request.POST.getlist('data_approve')
    data_sign = request.POST.getlist('data_sign')
    conid = request.POST.get('conid')

    countersign = json.loads(data_countersign[0])
    approve = json.loads(data_approve[0])
    sign = json.loads(data_sign[0])

    processConidEntity = models.contract.objects.filter(conid=conid)[0]

    for countersignusername in countersign:
        processCountersignUsernameEntity = models.user.objects.filter(username=countersignusername)[0]
        models.contract_process.objects.filter(conid=processConidEntity, username=processCountersignUsernameEntity,
                                               type=1, state=0, content="").update()

    for approveusername in approve:
        processApproveUsernameEntity = models.user.objects.filter(username=approveusername)[0]
        models.contract_process.objects.create(conid=processConidEntity, username=processApproveUsernameEntity, type=2,
                                               state=0, content="").save()

    for signusername in sign:
        processSignUsernameEntity = models.user.objects.filter(username=signusername)[0]
        models.contract_process.objects.create(conid=processConidEntity, username=processSignUsernameEntity, type=3,
                                               state=0, content="").save()

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
        authorized_rolename = models.right.objects.filter(username=authorized_username)[0].rolename.rolename
        response['authorized_rolename'] = authorized_rolename
        return render(request, 'CMSapp/authority_assignment.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


def data_updateAuthority(request):
    username = request.POST.get('username')
    new_rolename = request.POST.get('new_rolename')
    models.right.objects.filter(username=username).update(rolename=new_rolename)
    return HttpResponse(request)
