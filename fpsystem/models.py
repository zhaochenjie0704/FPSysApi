from django.db import models

# Create your models here.
#出退勤記録
class records(models.Model):
    class Meta:
        db_table = 'TBL_SYUTAIKIN_RECORD'
    #番号
    No = models.IntegerField(blank=False, default=1,unique=True)
    #作成者	
    SAKUSEISHA= models.CharField(max_length=70, blank=False, default='')
    #作成年月日								
    SAKUSEIYMD = models.DateField()
    								
    KOUSINSHA = models.CharField(max_length=70, blank=False, default='')
    KOUSINYMD = models.DateField()
    EMPLOYEEID = models.CharField(max_length=70, blank=False, default='')
    DAKOKU_TIME = models.DateField()
    KUBUN = models.CharField(max_length=70, blank=False, default='')
#基本情報
class kihonjyouhou(models.Model):
    class Meta:
        db_table = 'MST_KIHONJYOUHOU'
    SAKUSEISHA= models.CharField(max_length=70, blank=False, default='')
    SAKUSEIYMD= models.DateField()
    KOUSINSHA= models.CharField(max_length=70, blank=False, default='')
    KOUSINYMD= models.DateField()
    EMPLOYEEID= models.CharField(max_length=70, blank=False, default='', unique=True)
    NAME= models.CharField(max_length=70, blank=False, default='')
    SEX= models.CharField(max_length=70, blank=False, default='')
    BIRTHDAY= models.DateField()
    JOBGRADE= models.CharField(max_length=70, blank=False, default='')
    STATUS= models.CharField(max_length=70, blank=False, default='')
    ROLE_ID= models.CharField(max_length=70, blank=False, default='')
    CAPTURE = models.CharField(max_length=70, blank=False, default='')
    DEPARTMENT_CODE= models.CharField(max_length=70, blank=False, default='')
    ROOM_NO= models.CharField(max_length=70, blank=False, default='')
#部門
class bumon(models.Model):
    class Meta:
        db_table = 'MST_BUMON'
    SAKUSEISHA= models.CharField(max_length=70, blank=False, default='')
    SAKUSEIYMD= models.DateField()
    KOUSINSHA= models.CharField(max_length=70, blank=False, default='')
    KOUSINYMD= models.DateField()
    DEPARTMENT_CODE= models.CharField(max_length=70, blank=False, default='', unique=True)
    DEPARTMENT_NAME= models.CharField(max_length=70, blank=False, default='')
#ルーム
class room(models.Model):
    class Meta:
        db_table = 'MST_ROOM'
    SAKUSEISHA= models.CharField(max_length=70, blank=False, default='')
    SAKUSEIYMD= models.DateField()
    KOUSINSHA= models.CharField(max_length=70, blank=False, default='')
    KOUSINYMD= models.DateField()
    ROOM_NO= models.CharField(max_length=70, blank=False, default='', unique=True)
    ROOM_NAME= models.CharField(max_length=70, blank=False, default='')
#権限
class permission(models.Model):
    class Meta:
        db_table = 'MST_PERMISSION'
    EMPLOYEEID= models.CharField(max_length=70, blank=False, default='', unique=True)
    PASSWORD= models.CharField(max_length=70, blank=False, default='')
    MODIFIED_YMD= models.DateField()
    EXPIRED_DAYS=models.IntegerField(blank=False, default=30,unique=True)
    ROLE_ID= models.CharField(max_length=70, blank=False, default='')
    ROLE_NAME= models.CharField(max_length=70, blank=False, default='')