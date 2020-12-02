from django.http import HttpResponse
from django.shortcuts import render
from CMSapp.models import user
from django.http import JsonResponse
from django.shortcuts import redirect


# Create your views here.

def view_login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    return render(request,'CMSapp/login.html')


def view_register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    return render(request,'CMSapp/register.html')

def index(request):
    if request.session.get('is_login', None):
        return render(request, 'CMSapp/index.html')
    else:
        return redirect('/login/')

def view_draft(request):
    if request.session.get('is_login', None):
        return render(request, 'CMSapp/draft_contract.html')
    return render(request,'CMSapp/login.html')


def ajax_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(request)
    print(username)
    response = {}

    exists_username = user.objects.filter(username = username)
    print(exists_username)
    right_password = user.objects.filter(username = username, password = password)

    if exists_username:
        response['exists_username'] = 'success'
        if right_password:
            response['right_password'] = 'success'
            request.session['is_login'] = True
            request.session['username'] = username
        else:
            response['right_password'] = 'fail'
    else:
        response['exists_username'] = 'fail'

    return JsonResponse(response)


def ajax_confirm_username(request):
    username = request.POST.get('username')
    response = {'same_username': 'false'}

    same_username = user.objects.filter(username=username)

    if same_username:
        response['same_username'] = 'success'
    else:
        response['same_username'] = 'fail'

    return JsonResponse(response)


def ajax_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # confirm_password = request.POST.get('confirm_password')
    response = {'same_username': 'false'}

    same_username = user.objects.filter(username = username)
    print(same_username)

    if same_username:
        response['same_username'] = 'success'
    else:
        response['same_username'] = 'fail'

    if not same_username:
        user.objects.create(username = username, password = password).save()

    return JsonResponse(response)

def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'CMSapp/login.html')
    request.session['is_login'] = False
    request.session.flush()
    return render(request, 'CMSapp/login.html')

