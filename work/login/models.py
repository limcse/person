from django.db import models
from django.core.exceptions import ValidationError
import django.utils.timezone as timezone
import xadmin
# Create your models here.


class User(models.Model):

	card  = models.CharField(verbose_name='卡号',default='', unique=True,max_length=10)

	name  = models.CharField(verbose_name='姓名',default='', max_length=10)

	unit = models.CharField(max_length=20,default='',verbose_name='单位名称',blank=True)

	job_name = models.CharField(max_length=20,verbose_name='工种名称',default='', blank=True)

	level = models.CharField(max_length=10,default='', verbose_name='级别',blank=True)

	kind = models.CharField( max_length=10,default='', verbose_name='用工种类',blank=True)

	education = models.CharField(max_length=10,default='',verbose_name='学历',blank=True)

	birthday = models.DateField(verbose_name='出生日期',blank=True,default='')

	blood = models.CharField(max_length=8,default='',verbose_name='血型',blank=True)

	identity =  models.CharField(max_length=18,verbose_name='身份证号码',blank=True,default='')

	address  = models.CharField(verbose_name='家庭住址', max_length=100,blank=True,default='')

	gh  = models.CharField(verbose_name='工号',max_length=10,blank=True,default='')

	marriage = models.CharField(max_length=8,default='已婚',verbose_name='婚姻状况',blank=True)

	phone = models.CharField(verbose_name='手机', max_length=11,blank=True,default='')

	job_time = models.DateField(verbose_name='参加工作时间',blank=True,default='')

	native  = models.CharField(verbose_name='籍贯', max_length=50,blank=True,default='')

	content  = models.CharField(verbose_name='备注',default='',max_length=100,blank=True)

	def __str__(self):

		return self.name

	class Meta:

		ordering=['card']
	
		verbose_name = "员工信息"

		verbose_name_plural = "员工信息"

