import os
from datetime import datetime, timezone, timedelta

import django
from django.db.models import Q
import pytz
from django.http import JsonResponse, FileResponse
from django.shortcuts import render, HttpResponse
from django.utils.encoding import escape_uri_path

from CMSapp import models
import json

from CMSapp.forms import UploadFileForm

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

        response['contractState'] = models.contract_state.objects.filter(conid=allocation_conid)[0].type

        canCountersignRoles = models.role_function.objects.filter(function='contract_countersign')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid, type=1)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left1_rightlist = models.right.objects.filter(rolename__rolename__in=canCountersignRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canApprovalRoles = models.role_function.objects.filter(function='contract_approval')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid, type=2)
        noManageTheContractUserlist = models.user.objects.exclude(
            username__in=manageTheContractUserlist.values('username'))
        left2_rightlist = models.right.objects.filter(rolename__rolename__in=canApprovalRoles.values('rolename'),
                                                      username__username__in=noManageTheContractUserlist.values(
                                                          'username'))

        canSignRoles = models.role_function.objects.filter(function='contract_sign')
        manageTheContractUserlist = models.contract_process.objects.filter(conid=allocation_conid, type=3)
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
    username = request.session.get('username')
    countersign = json.loads(data_countersign[0])
    approve = json.loads(data_approve[0])
    sign = json.loads(data_sign[0])
    conname=models.contract.objects.filter(conid=conid)[0]
    processConidEntity = models.contract.objects.filter(conid=conid)[0]

    # 删除process数据库中还未开始会签的人员数据
    models.contract_process.objects.filter(conid=conid, type=1, state=0).delete()  # 把还未开始的会签员都删了
    # 重新根据前端返回的会签人员列表进行分配
    for countersignusername in countersign:
        try:
            processCountersignUsernameEntity = models.user.objects.filter(username=countersignusername)[0]
            models.contract_process.objects.create(conid=processConidEntity, username=processCountersignUsernameEntity,
                                                   type=1, state=0, content="").save()
            models.log.objects.create(username=username, operateobject='合同编号: ' + conid + ' 合同名: ' + conname.conname,
                                      content=' 分配会签人员: ' + countersignusername).save()
        except:
            pass

    models.contract_process.objects.filter(conid=conid, type=2, state=0).delete()
    for approveusername in approve:
        try:
            processApproveUsernameEntity = models.user.objects.filter(username=approveusername)[0]
            models.contract_process.objects.create(conid=processConidEntity, username=processApproveUsernameEntity,
                                                   type=2, state=0, content="").save()
            models.log.objects.create(username=username, operateobject='合同编号: ' + conid + ' 合同名: ' + conname.conname,
                                      content=' 分配审批人员: ' + approveusername).save()

        except:
            pass

    models.contract_process.objects.filter(conid=conid, type=3, state=0).delete()
    for signusername in sign:
        try:
            processSignUsernameEntity = models.user.objects.filter(username=signusername)[0]
            models.contract_process.objects.create(conid=processConidEntity, username=processSignUsernameEntity, type=3,
                                                   state=0, content="").save()
            models.log.objects.create(username=username, operateobject='合同编号: ' + conid + ' 合同名: ' + conname.conname,
                                      content=' 分配签订人员: ' + signusername).save()
        except:
            pass


    currentContactState = models.contract_state.objects.get(conid=conid).type

    if currentContactState == 1:
        # 判断是否会签完成
        countersignernum = len(models.contract_process.objects.filter(conid_id=conid, type=1))  # 合同所有会签人数
        countersignernum_finish = len(
            models.contract_process.objects.filter(conid_id=conid, type=1, state=1))  # 合同所有会签已完成的人数
        if countersignernum == countersignernum_finish:
            updateStateData = models.contract_state.objects.filter(conid=conid)[0]  # .update(type=2)
            updateStateData.type = 2
            updateStateData.save()


    if currentContactState == 4:
        # 判断是否签订完成
        approvalnum = len(models.contract_process.objects.filter(conid_id=conid, type=3))  # 合同所有签订人数
        approvednum = len(models.contract_process.objects.filter(conid_id=conid, type=3, state=1))  # 合同所有签订已完成的人数
        if approvalnum == approvednum:
            updateDataState = models.contract_state.objects.filter(conid=conid)[0]  # .update(type=5)
            updateDataState.type = 5
            updateDataState.save()

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
    operatername=request.session.get('username')
    username = request.POST.get('username')
    new_rolename = request.POST.get('new_rolename')

    # 如果该用户起草的合同还有未审批完成的，则提示不能更改

    # 如果该用户参与了其他人起草的合同，则提示先替换
    models.right.objects.filter(username=username).update(rolename=new_rolename)
    models.log.objects.create(username=operatername, operateobject='用户姓名: ' + username,
                              content=' 授权: '+new_rolename).save()
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
    username = request.session.get('username')

    if cusid:
        models.customer.objects.filter(cusid=cusid).update(cusname=cusname, address=address, tel=tel, code=code,
                                                           fax=fax, bank=bank,
                                                           account=account)
        models.log.objects.create(username=username, operateobject='客户编号: '+cusid+" 客户姓名: "+cusname ,
                                  content=' 更新客户信息').save()
    else:
        customer=models.customer.objects.create(cusname=cusname, address=address, tel=tel, code=code, fax=fax, bank=bank,
                                       account=account)
        models.log.objects.create(username=username, operateobject='客户编号: ' + str(customer.cusid) + " 客户姓名: " + cusname,
                                  content=' 新增客户').save()
    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
# 合同审批信息
def data_contract_approval(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        response['approver'] = request.POST.get('approver')
        return render(request, 'CMSapp/contract_approval.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################
# 更新合同审批信息
def data_updateContractApprovalmsg(request):
    conid = request.POST.get('conid')
    state = request.POST.get('state')
    content = request.POST.get('content')
    contractEntity = models.contract.objects.filter(conid=conid)[0]
    # user = models.user.objects.filter(username=request.session.get('username'))[0]
    approver = request.POST.get('approver')
    username = request.session.get('username')
    updateDataProcess = models.contract_process.objects.filter(conid=conid, username=approver, type=2)[0]
    updateDataState = models.contract_state.objects.filter(conid=conid)[0]
    if state == 'true':
        # models.contract_process.objects.filter(conid=contractEntity, username=user, type=2).update(state=1,content=content)
        # models.contract_state.objects.filter(conid=contractEntity).update(type=4)
        updateDataProcess.state = 1
        updateDataProcess.content = content
        updateDataProcess.save()
        updateDataState.type = 4
        updateDataState.save()
        models.log.objects.create(username=username,
                                  operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                                  content=' 审批通过').save()
    else:  # 审批未通过
        # models.contract_process.objects.filter(conid=contractEntity, username=user, type=2).update(state=2,content=content)
        # models.contract_state.objects.filter(conid=contractEntity).update(type=2)   # 改为会签已完成状态（待定稿）
        updateDataProcess.state = 2
        updateDataProcess.content = content
        updateDataProcess.save()
        updateDataState.type = 2
        updateDataState.save()
        models.log.objects.create(username=username,
                                  operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                                  content=' 审批未通过').save()

    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
# 合同签订信息
def data_contract_sign(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        customerMsg = models.customer.objects.filter(cusid=contractMsg.cusid_id)[0]
        response['customerMsg'] = customerMsg
        response['signer'] = request.POST.get('signer')
        return render(request, 'CMSapp/contract_sign.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################

# 更新合同签订信息
def data_updateContractSignmsg(request):
    conid = request.POST.get('conid')
    username=request.session.get('username')
    signer = request.POST.get('signer')
    information = request.POST.get('information')
    updateDataProcess = models.contract_process.objects.filter(conid=conid, username=signer, type=3)[
        0]  # .update(state=1,content=information)
    contractEntity = models.contract.objects.filter(conid=conid)[0]
    updateDataProcess.state = 1
    updateDataProcess.content = information
    updateDataProcess.save()

    approvalnum = len(models.contract_process.objects.filter(conid_id=conid, type=3))  # 合同所有签订人数
    approvednum = len(models.contract_process.objects.filter(conid_id=conid, type=3, state=1))  # 合同所有签订已完成的人数

    if approvalnum == approvednum:
        updateDataState = models.contract_state.objects.filter(conid=conid)[0]  # .update(type=5)
        updateDataState.type = 5
        updateDataState.save()
        models.log.objects.create(username=username,
                                  operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                                  content=' 签订成功').save()
    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################
# 添加合同信息界面
def data_contractmsg(request):
    if request.session.get('is_login', None):
        response = {}
        conname = request.POST.get('conname')
        begintime = request.POST.get('begintime')
        endtime = request.POST.get('endtime')
        content = request.POST.get('content')
        # file_upload = request.FILES.get('file_upload')
        # file_name = request.FILES.get('file_name')
        # file_extname = request.FILES.get('file_extname')

        cusid = models.customer.objects.filter(cusid=request.POST.get('cusid'))[0]
        username = models.user.objects.filter(username=request.session.get('username'))[0]
        contract = models.contract.objects.create(conname=conname, begintime=begintime, endtime=endtime,
                                                  content=content,
                                                  cusid=cusid, username=username)
        contract_type = 1
        models.contract_state.objects.create(type=contract_type, conid=contract).save()
        models.log.objects.create(username=username.username,
                                  operateobject='合同编号: ' + str(contract.conid) + " 合同名称: " + contract.conname,
                                  content=' 起草成功').save()

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('进入valid')
            filename = form.cleaned_data['filename']
            filetype = form.cleaned_data['filetype']
            file = form.cleaned_data['file']
            models.contract_attachment.objects.create(conid= contract,filename=filename, filetype=filetype, file=file).save()
            models.log.objects.create(username=username,
                                      operateobject='合同编号: ' + contract.conid + " 合同名称: " + contract.conname,
                                      content=' 附件添加成功').save()

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
        response['countersignSuggestList'] = countersignSuggestList
        return render(request, 'CMSapp/final_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################

# 更新合同定稿信息
def data_updateContractFinalMsg(request):
    conid = request.POST.get('conid')
    content = request.POST.get('content')
    username = request.session.get('username')
    contractEntity = models.contract.objects.filter(conid=conid)[0]
    constate = models.contract_state.objects.filter(conid=conid)[0]
    constate.type = 3
    constate.save()
    models.contract.objects.filter(conid=conid).update(content=content)
    models.log.objects.create(username=username,
                              operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                              content=' 定稿成功').save()
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
        response['contersigner'] = request.POST.get('contersigner')
        return render(request, 'CMSapp/countersign_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################

# 更新合同会签信息
def data_updateContractCountersignMsg(request):
    conid = request.POST.get('conid')
    contersigner = request.POST.get('contersigner')
    username=request.session.get('username')
    single_content = request.POST.get('single_content')

    contractEntity = models.contract.objects.filter(conid=conid)[0]
    updateProcessData = models.contract_process.objects.filter(conid=conid, type=1, username=contersigner)[
        0]  # .update(content=single_content,state=1)
    updateProcessData.content = single_content
    updateProcessData.state = 1
    updateProcessData.save()
    models.log.objects.create(username=username,
                              operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                              content=' 会签成功').save()

    # 判断是否所有会签人通过
    countersignernum = len(models.contract_process.objects.filter(conid_id=conid, type=1))  # 合同所有会签人数
    countersignernum_finish = len(
        models.contract_process.objects.filter(conid_id=conid, type=1, state=1))  # 合同所有会签已完成的人数

    if countersignernum == countersignernum_finish:
        updateStateData = models.contract_state.objects.filter(conid=contractEntity)[0]  # .update(type=2)
        updateStateData.type = 2
        updateStateData.save()
        models.log.objects.create(username=username,
                                  operateobject='合同编号: ' + str(contractEntity.conid) + " 合同名称: " + contractEntity.conname,
                                  content=' 会签全体通过').save()

    return HttpResponse(request)


################################################################################################################
################################################################################################################
################################################################################################################

# 合同详情页
def contractDetail(request):
    if request.session.get('is_login', None):
        response = {}
        conid = request.POST.get('keyword')
        contractMsg = models.contract.objects.filter(conid=conid)[0]
        response['contractMsg'] = contractMsg
        customerMsg = models.customer.objects.filter(cusid=contractMsg.cusid_id)[0]
        response['customerMsg'] = customerMsg

        fileResultlist = models.contract_attachment.objects.filter(conid=conid)
        if fileResultlist:
            response['has_attachment']='true'
        else:
            response['has_attachment'] = 'false'
        return render(request, 'CMSapp/contract_detail.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


# 下载附件
def downloadFile(request,conid):
    if request.session.get('is_login', None):
        fileResultlist  = models.contract_attachment.objects.filter(conid=conid)
        if fileResultlist:
            fileEntity = fileResultlist[0]
            filepath = 'uploadfile/'+str(fileEntity.file)
            file = open(filepath, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename={0}'.format(escape_uri_path(fileEntity.filename))
            return response
        else:
            return HttpResponse("无附件")
    else:
        return render(request, 'CMSapp/timeout.html')


################################################################################################################
################################################################################################################
################################################################################################################

