from django.db import models


# Create your models here.

# 用户基本信息
class user(models.Model):
    username = models.CharField(primary_key=True, max_length=40)    # 用户名
    password = models.CharField(max_length=20)                      # 密码


# 角色信息
class role(models.Model):
    rolename = models.CharField(primary_key=True, max_length=40)    # 角色名
    description = models.CharField(max_length=100)                  # 角色描述


# 权限信息
class right(models.Model):
    username = models.OneToOneField("user", on_delete=models.CASCADE)       # 用户名
    rolename = models.ForeignKey("role", on_delete=models.CASCADE)          # 角色名
    description = models.CharField(max_length=100, null=True, blank=True)   # 描述


# 功能信息
class function(models.Model):
    funcname = models.CharField(primary_key=True, max_length=40, unique=True)   # 功能名
    url = models.CharField(max_length=100)                                      # 操作url
    description = models.CharField(max_length=100)                              # 描述


# 角色功能信息
class role_function(models.Model):
    rolename = models.ForeignKey("role", on_delete=models.CASCADE)              # 角色名
    function = models.ForeignKey("function", on_delete=models.CASCADE)          # 功能

    class Meta:
        unique_together = ("rolename", "function")  # 类似多字段主键


# 客户信息表
class customer(models.Model):
    cusid = models.AutoField(primary_key=True)                          # 客户id
    cusname = models.CharField(max_length=40)                           # 客户名
    address = models.CharField(max_length=100)                          # 地址
    tel = models.CharField(max_length=20)                               # 电话
    fax = models.CharField(max_length=20, null=True, blank=True)        # 传真
    code = models.CharField(max_length=6, null=True, blank=True)        # 邮编
    bank = models.CharField(max_length=50, null=True, blank=True)       # 银行
    account = models.CharField(max_length=20, null=True, blank=True)    # 银行账户


# 合同基本信息
class contract(models.Model):
    conid = models.AutoField(primary_key=True)                          # 合同id
    conname = models.CharField(max_length=40)                           # 合同名称
    cusid = models.ForeignKey("customer", on_delete=models.CASCADE)     # 客户编号
    begintime = models.DateField()                                      # 合同开始时间
    endtime = models.DateField()                                        # 合同结束时间
    content = models.TextField()                                        # 合同内容
    username = models.ForeignKey("user", on_delete=models.CASCADE)      # 起草人


# 合同操作流程信息
class contract_process(models.Model):
    conid = models.ForeignKey("contract", on_delete=models.CASCADE)     # 合同id
    username = models.ForeignKey("user", on_delete=models.CASCADE)      # 起草人
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
    type = models.IntegerField(choices=type_choice)                     # 操作类型
    state = models.IntegerField(choices=state_choice, default=0)        # 操作状态
    content = models.TextField(null=True, blank=True)                   # 内容（不同操作类型填的内容不同，签订就填签订内容，审批就填审批意见）
    modifytime = models.DateTimeField(auto_now=True)                    # 最后修改时间

    class Meta:
        unique_together = ("conid", "username", "type")  # 类似多字段主键


# 合同操作状态信息
class contract_state(models.Model):
    conid = models.OneToOneField("contract", on_delete=models.CASCADE)  # 合同id
    state_choice = (
        (1, "起草"),
        (2, "会签完成"),
        (3, "定稿完成"),
        (4, "审批完成"),
        (5, "签订完成"),
        (6, "已作废"),
    )
    type = models.IntegerField(choices=state_choice)                    # 合同当前状态
    modifytime = models.DateTimeField(auto_now=True)                    # 最后修改时间


# 日志信息
class log(models.Model):
    username = models.CharField(max_length=40)          # 用户名
    operateobject = models.CharField(max_length=40)     # 操作对象
    content = models.TextField()                        # 操作内容
    operatetime = models.DateTimeField(auto_now=True)   # 操作时间


# 合同附件基本信息
class contract_attachment(models.Model):
    conid = models.ForeignKey("contract", on_delete=models.CASCADE)     # 合同id
    filename = models.CharField(max_length=100)                         # 文件名
    filetype = models.CharField(max_length=20)                          # 文件类型
    file = models.FileField(upload_to='CMSapp/%Y/%m/%d')                # 文件路径
    uploadtime = models.DateTimeField(auto_now=True)                    # 上传时间

