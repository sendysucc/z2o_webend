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
    agentid = models.ForeignKey('Agent',db_column='agentid',blank=True,null=True,on_delete=models.SET_NULL)
    promotecode = models.CharField('推广码'，max_length=10)
    referrer = models.CharField('推荐人', max_length = 10)
    accountdisable = models.BooleanField('账号是否被封',default=False)
    isrobot = models.BooleanField('是否为机器人', default=False)

    class Meta:
        db_table = 'User'


class Agent(models.Model):
    agentid = models.AutoField(primary_key=True)
    name = models.CharField('代理名',max_length=30)
    acode = models.CharField('代理编码', max_length=20)
    cellphone = models.CharField('手机号',max_length=11)
    password = models.CharField('密码', max_length=40)
    gold = models.IntegerField('金币')
    diamond = models.IntegerField('钻石')
    createtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Agent'


