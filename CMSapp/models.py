from django.db import models


# Create your models here.

# 用户基本信息
class user(models.Model):
    username = models.CharField(primary_key=True, max_length=40)
    password = models.CharField(max_length=20)


# 角色信息
class role(models.Model):
    rolename = models.CharField(primary_key=True, max_length=40)
    description = models.CharField(max_length=100)


# 权限信息
class right(models.Model):
    username = models.OneToOneField("user", on_delete=models.CASCADE)
    rolename = models.ForeignKey("role", on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)


# 功能信息
class function(models.Model):
    funcname = models.CharField(primary_key=True, max_length=40, unique=True)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


# 角色功能信息
class role_function(models.Model):
    rolename = models.ForeignKey("role", on_delete=models.CASCADE)
    function = models.ForeignKey("function", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("rolename", "function")  # 类似多字段主键


# 客户信息表
class customer(models.Model):
    cusid = models.AutoField(primary_key=True)
    cusname = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, null=True, blank=True)
    code = models.CharField(max_length=6, null=True, blank=True)  # 邮编
    bank = models.CharField(max_length=50, null=True, blank=True)
    account = models.CharField(max_length=20, null=True, blank=True)


# 合同基本信息
class contract(models.Model):
    conid = models.AutoField(primary_key=True)
    conname = models.CharField(max_length=40)
    cusid = models.ForeignKey("customer", on_delete=models.CASCADE)
    begintime = models.DateField()
    endtime = models.DateField()
    content = models.TextField()
    username = models.ForeignKey("user", on_delete=models.CASCADE)  # 起草人


# 合同操作流程信息
class contract_process(models.Model):
    conid = models.ForeignKey("contract", on_delete=models.CASCADE)
    username = models.ForeignKey("user", on_delete=models.CASCADE)
    type_choice = (
        (1, "会签"),
        (2, "审批"),
        (3, "签订"),
    )
    state_choice = (
        (0, "未完成"),
        (1, "已完成"),
        (2, "已否决"),
    )
    type = models.IntegerField(choices=type_choice)
    state = models.IntegerField(choices=state_choice, default=0)
    content = models.TextField(null=True, blank=True)
    modifytime = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("conid", "username", "type")  # 类似多字段主键


# 合同操作状态信息
class contract_state(models.Model):
    conid = models.OneToOneField("contract", on_delete=models.CASCADE)
    state_choice = (
        (1, "起草"),
        (2, "会签完成"),
        (3, "定稿完成"),
        (4, "审批完成"),
        (5, "签订完成"),
    )
    type = models.IntegerField(choices=state_choice)
    modifytime = models.DateTimeField(auto_now=True)


# 日志信息
class log(models.Model):
    username = models.CharField(max_length=40)
    content = models.TextField()
    operatetime = models.DateTimeField(auto_now=True)


# 合同附件基本信息
class contract_attachment(models.Model):
    conid = models.ForeignKey("contract", on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    filetype = models.CharField(max_length=20)
    file = models.FileField(upload_to='CMSapp/%Y/%m/%d')
    uploadtime = models.DateTimeField(auto_now=True)
