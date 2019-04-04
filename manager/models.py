from django.db import models

# Create your models here.

class User(models.Model):
    GENDER = {
        ('男', 1),
        ('女',0),
    }

    userid = models.AutoField(primary_key=True)
    username = models.CharField('用户名',max_length=15)
    nickname = models.CharField('昵称',max_length=30)
    avatoridx = models.IntegerField('头像id')
    gender = models.IntegerField('性别', choices=GENDER)
    cellphone = models.CharField('手机号',max_length=11)
    password = models.CharField('密码',max_length=41)
    gold = models.IntegerField('金币')
    diamond = models.IntegerField('钻石')
    createtime = models.DateTimeField(auto_now=True)
    agentid = models.ForeignKey('Agenter',db_column='agentid',blank=True,null=True,on_delete=models.SET_NULL)   #对用户不可见，可根据app包或者url来标识
    promotecode = models.CharField('推广码',max_length=10)      #用户自己的推广码，用于推广给其他新用户，来获取收益
    referrer = models.CharField('推荐人', max_length = 10)      #注册时的推荐人， 就是其他用户的推广码
    accountdisable = models.BooleanField('账号是否被封',default=False)
    isrobot = models.BooleanField('是否为机器人', default=False)

    class Meta:
        db_table = 'User'


class Agenter(models.Model):
    agentid = models.AutoField(primary_key=True)
    name = models.CharField('代理名',max_length=30)
    acode = models.CharField('代理编码', max_length=20)
    cellphone = models.CharField('手机号',max_length=11)
    password = models.CharField('密码', max_length=40)
    gold = models.IntegerField('金币')
    diamond = models.IntegerField('钻石')
    createtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Agenter'

class LoginRecord(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', db_column='userid',blank=True, null=True, on_delete=models.SET_NULL)
    logintime = models.DateTimeField(auto_now=True)
    ipaddr = models.CharField(max_length=32)

    class Meta:
        db_table = 'LoginRecord'

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharFiled(max_length=30)
    msg = models.CharField(max_length=300)
    pubtime = models.DateTimeField()

    class Meta:
        db_table = 'Notice'

class Mail(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.CharField(max_length=30)
    msg = models.TextField()
    pubtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Mail'

