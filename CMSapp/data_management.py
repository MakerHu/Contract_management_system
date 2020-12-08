import os
from datetime import datetime, timezone, timedelta

import django
from django.db.models import Q
import pytz
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
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid,type=1)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left1_rightlist = models.right.objects.filter(rolename__rolename__in=canCountersignRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canApprovalRoles = models.role_function.objects.filter(function='contract_approval')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid,type=2)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left2_rightlist = models.right.objects.filter(rolename__rolename__in=canApprovalRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canSignRoles = models.role_function.objects.filter(function='contract_sign')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid,type=3)
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

    # 删除process数据库中还未开始会签的人员数据
    models.contract_process.objects.filter(conid=conid, type=1, state=0).delete()
    # 重新根据前端返回的会签人员列表进行分配
    for countersignusername in countersign:
        processCountersignUsernameEntity = models.user.objects.filter(username=countersignusername)[0]
        models.contract_process.objects.create(conid=processConidEntity, username=processCountersignUsernameEntity,
                                                   type=1, state=0, content="").save()

    models.contract_process.objects.filter(conid=conid, type=2, state=0).delete()
    for approveusername in approve:
        processApproveUsernameEntity = models.user.objects.filter(username=approveusername)[0]
        models.contract_process.objects.create(conid=processConidEntity, username=processApproveUsernameEntity, type=2,
                                               state=0, content="").save()

    models.contract_process.objects.filter(conid=conid, type=3, state=0).delete()
    for signusername in sign:
        processSignUsernameEntity = models.user.objects.filter(username=signusername)[0]
        models.contract_process.objects.create(conid=processConidEntity, username=processSignUsernameEntity, type=3,
                                               state=0, content="").save()

    response = {'is': 'success'}

    return JsonResponse(response)


################################################################################################################
################################################################################################################
################################################################################################################
# 返回授权信息填写表
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


# 更新授权信息
def data_updateAuthority(request):
    username = request.POST.get('username')
    new_rolename = request.POST.get('new_rolename')
    models.right.objects.filter(username=username).update(rolename=new_rolename)
    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
# 添加客户信息界面
def data_customermsg(request):
    if request.session.get('is_login', None):
        response = {}
        cusid = request.POST.get('keyword')
        if cusid:
            response['type'] = 'detail'
            customerMsg = models.customer.objects.filter(cusid=cusid)[0]
            response['customerMsg'] = customerMsg
        else:
            response['type'] = 'add'
        return render(request, 'CMSapp/customer_msg.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


# 更新客户信息
def data_updateCustomermsg(request):
    cusid = request.POST.get('cusid')
    cusname = request.POST.get('cusname')
    address = request.POST.get('address')
    tel = request.POST.get('tel')
    code = request.POST.get('code')
    fax = request.POST.get('fax')
    bank = request.POST.get('bank')
    account = request.POST.get('account')

    if cusid:
        models.customer.objects.filter(cusid=cusid).update(cusname=cusname, address=address, tel=tel, code=code,
                                                           fax=fax, bank=bank,
                                                           account=account)
    else:
        models.customer.objects.create(cusname=cusname, address=address, tel=tel, code=code, fax=fax, bank=bank,
                                       account=account).save()
    return HttpResponse(request)

################################################################################################################
################################################################################################################
################################################################################################################
#合同审批信息
def data_contract_approval(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        return render(request, 'CMSapp/contract_approval.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')

################################################################################################################
################################################################################################################
################################################################################################################
#更新合同审批信息
def data_updateContractApprovalmsg(request):
    conid = request.POST.get('conid')
    state = request.POST.get('state')
    content = request.POST.get('content')
    contractEntity = models.contract.objects.filter(conid=conid)[0]
    user = models.user.objects.filter(username=request.session.get('username'))[0]
    if state == 'true':
        models.contract_state.objects.filter(conid=contractEntity).update(type=4)
        print(contractEntity)
        print(user)
        models.contract_process.objects.filter(conid=contractEntity, username=user, type=2).update(state=1, content=content)
    else:
        models.contract_state.objects.filter(conid=contractEntity).update(type=4)
        models.contract_process.objects.filter(conid=contractEntity, username=user, type=2).update(state=2, content=content)


    models.contract_state.objects.filter(conid=contractEntity).update(type=4)
    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
#合同签订信息
def data_contract_sign(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        customerMsg = models.customer.objects.filter(cusid=contractMsg.cusid_id)[0]
        response['customerMsg'] = customerMsg
        return render(request, 'CMSapp/contract_sign.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')

################################################################################################################
################################################################################################################
################################################################################################################

#更新合同签订信息
def data_updateContractSignmsg(request):
    conid = request.POST.get('conid')
    username=request.session.get('username')
    information = request.POST.get('information')
    models.contract_process.objects.filter(conid=conid,username=username,type=3).update(state=1,content=information)

    approvalnum = len(models.contract_process.objects.filter(conid_id=conid, type=3)) #合同所有审批人数
    approvednum = len(models.contract_process.objects.filter(conid_id=conid, type=3, state=1))# 合同所有已审批已完成的人数

    if approvalnum==approvednum:
        models.contract_state.objects.filter(conid=conid).update(type=5)

    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
# 添加合同信息界面
def data_contractmsg(request):
    if request.session.get('is_login', None):
        response = {}
        conname=request.POST.get('conname')
        begintime = request.POST.get('begintime')
        endtime = request.POST.get('endtime')
        content = request.POST.get('content')
        cusid = models.customer.objects.filter(cusid=request.POST.get('cusid'))[0]
        username = models.user.objects.filter(username=request.session.get('username'))[0]
        contract = models.contract.objects.create(conname=conname, begintime=begintime, endtime=endtime, content=content,
                                       cusid=cusid, username=username)
        dt = datetime.utcnow()
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        contract_type = 1
        models.contract_state.objects.create(type=contract_type, modifytime=local_dt, conid=contract).save()
        return render(request, 'CMSapp/draft_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################
# 定稿
def contract_finalize(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        customerMsg = models.customer.objects.filter(cusid=contractMsg.cusid_id)[0]
        response['customerMsg'] = customerMsg
        countersignSuggestList = models.contract_process.objects.filter(conid=conid, type=1, state=1)
        response['countersignSuggestList']=countersignSuggestList
        return render(request, 'CMSapp/final_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')

################################################################################################################
################################################################################################################
################################################################################################################

#更新合同定稿信息
def data_updateContractFinalMsg(request):
    conid = request.POST.get('conid')
    content = request.POST.get('content')
    models.contract_state.objects.filter(conid=conid).update(type=3)
    models.contract.objects.filter(conid=conid).update(content=content)
    return HttpResponse(request)

################################################################################################################
################################################################################################################
################################################################################################################
# 会签
def contract_countersign(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        customerMsg = models.customer.objects.filter(cusid=contractMsg.cusid_id)[0]
        response['customerMsg'] = customerMsg
        return render(request, 'CMSapp/countersign_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')

################################################################################################################
################################################################################################################
################################################################################################################

#更新合同会签信息
def data_updateContractCountersignMsg(request):
    conid = request.POST.get('conid')
    username=request.session.get('username')
    single_content = request.POST.get('single_content')
    contractEntity = models.contract.objects.filter(conid=conid)[0]
    if(~Q(models.contract_process.objects.filter(conid=conid,type=1,state=0).exists())):
        models.contract_state.objects.filter(conid=contractEntity).update(type=2)
    models.contract_process.objects.filter(conid=conid,type=1,username=username).update(content=single_content)
    models.contract_process.objects.filter(conid=conid,type=1,username=username).update(state=1)
    return HttpResponse(request)
