import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Contract_management_system.settings")  # project_name 项目名称
django.setup()

from CMSapp import models

# 初始化角色表
models.role.objects.get_or_create(rolename='root', description='最高管理员')
models.role.objects.get_or_create(rolename='newuser', description='新用户')
models.role.objects.get_or_create(rolename='operater', description='操作员')

# 初始化功能表
models.function.objects.get_or_create(funcname='contract_draft', url='/contract_draft/', description='合同起草')
models.function.objects.get_or_create(funcname='contract_countersign', url='/contract_countersign/', description='合同会签')
models.function.objects.get_or_create(funcname='contract_approval', url='/contract_approval/', description='合同审批')
models.function.objects.get_or_create(funcname='contract_sign', url='/contract_sign/', description='合同签订')
models.function.objects.get_or_create(funcname='contract_distribute', url='/contract_distribute/', description='合同分配')
models.function.objects.get_or_create(funcname='customer_manage', url='/customer_manage/', description='客户管理')
models.function.objects.get_or_create(funcname='right_manage', url='/right_manage/', description='权限管理')



# 初始化角色权限表

# 实例化角色
root = models.role.objects.filter(rolename='root', description='最高管理员')[0]
newuser = models.role.objects.filter(rolename='newuser', description='新用户')[0]
operater = models.role.objects.filter(rolename='operater', description='操作员')[0]

# 实例化功能
contract_draft = models.function.objects.filter(funcname='contract_draft', url='/contract_draft/', description='合同起草')[0]
contract_countersign = models.function.objects.filter(funcname='contract_countersign', url='/contract_countersign/', description='合同会签')[0]
contract_approval = models.function.objects.filter(funcname='contract_approval', url='/contract_approval/', description='合同审批')[0]
contract_sign = models.function.objects.filter(funcname='contract_sign', url='/contract_sign/', description='合同签订')[0]
contract_distribute = models.function.objects.filter(funcname='contract_distribute', url='/contract_distribute/', description='合同分配')[0]
customer_manage = models.function.objects.filter(funcname='customer_manage', url='/customer_manage/', description='客户管理')[0]
right_manage = models.function.objects.filter(funcname='right_manage', url='/right_manage/', description='权限管理')[0]

models.role_function.objects.get_or_create(rolename=root, function=contract_draft)
models.role_function.objects.get_or_create(rolename=root, function=contract_countersign)
models.role_function.objects.get_or_create(rolename=root, function=contract_approval)
models.role_function.objects.get_or_create(rolename=root, function=contract_sign)
models.role_function.objects.get_or_create(rolename=root, function=contract_distribute)
models.role_function.objects.get_or_create(rolename=root, function=customer_manage)
models.role_function.objects.get_or_create(rolename=root, function=right_manage)

models.role_function.objects.get_or_create(rolename=operater, function=contract_draft)
models.role_function.objects.get_or_create(rolename=operater, function=contract_countersign)
models.role_function.objects.get_or_create(rolename=operater, function=contract_approval)
models.role_function.objects.get_or_create(rolename=operater, function=contract_sign)