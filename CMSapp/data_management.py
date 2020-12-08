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
        models.contract.objects.create(conname=conname, begintime=begintime, endtime=endtime, content=content,
                                       cusid=cusid, username=username).save()
        return render(request, 'CMSapp/draft_contract.html', response)
    else:
        return render(request, 'CMSapp/timeout.html')


