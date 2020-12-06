import os,django
from django.http import JsonResponse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")# project_name 项目名称
django.setup()



def data_draft_contract(request):
    pass


def test(request):
    countersign_person = request.POST.get('countersign_person')
    approve_person = request.POST.get('approve_person')
    sign_person = request.POST.get('sign_person')

    print('000000000000000000000000000000000')

    print('countersign_person')
    print(countersign_person)

    print('approve_person')
    print(approve_person)

    print('sign_person')
    print(sign_person)

    response = {'is': 'success'}


    return JsonResponse(response)


