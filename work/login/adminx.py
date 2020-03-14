
from xadmin import views
from django.http import HttpResponseRedirect
from xlrd import open_workbook
from . models import User
from datetime import datetime, date
import xadmin
# Register your models here.
#admin.site.site_title = "后台管理"
#admin.site.site_header = "五阳煤矿人员管理系统"
#('card','name','unit','job_name','level','kind','education','birthday','blood',
#'identity','address','gh','marriage','phone','job_time','native','content')

class user_serach(object):

		import_excel = False

		list_display = ['card','name','unit',]

		ordering =['card']

		search_fields=['name','card']

		list_editable = ['card','name','unit','job_name']

		list_export_fields = ('name',)
	#每页显示多少个
		list_per_page = 20
"""
		def post(self,request,*args,**kwargs):

			if 'excel' in request.FILES:
				execl_file = request.FILES.get('excel')
				wb = open_workbook(filename=None, file_contents=request.FILES['excel'].read())
				#tab = wb.sheets()[0]
				#rows = table.nrows
				#cols = table.ncols
				sheet = wb.sheet_by_index(0)
				tab = wb.sheet_by_name('Sheet1')
				cols = sheet.ncols
				rows = sheet.nrows
				for r in range(1,rows):
					card = tab.cell(r,0).value
					name = tab.cell(r,1).value
					unit = tab.cell(r,2).value
					job_name = tab.cell(r,3).value
					level = tab.cell(r,4).value
					kind = tab.cell(r,5).value
					education = tab.cell(r,6).value
					print(education)
					blood = tab.cell(r,8).value
					identity = tab.cell(r,9).value
					address = tab.cell(r,10).value
					gh = tab.cell(r,11).value
					marriage = tab.cell(r,12).value
					phone = tab.cell(r,13).value
					native = tab.cell(r,15).value
					content = tab.cell(r,16).value
					if tab.cell(r,7).ctype == 3:
						#print (tab.cell(r,7).value)
						birthday= xlrd.xldate.xldate_as_datetime(tab.cell(r,7).value,1)
						print(birthday)
						if tab.cell(r,14).ctype == 3:
							job_time= xlrd.xldate.xldate_as_datetime(tab.cell(r,14).value,1)
							print(job_time)
							User.objects.get_or_create(card=card,name=name,unit=unit,job_name=job_name,level=level,kind=kind,education=education,birthday=birthday,blood=blood,identity=identity,address=address,gh=gh,marriage=marriage,phone=phone,job_time=job_time,native=native,content=content)
				return HttpResponseRedirect('导入成功')
				return super(user_serach,self).post(request,args,kwargs)"""

xadmin.site.register(User,user_serach)

class GlobalSetting(object):
	site_title = "后台管理"
	site_footer = "五阳煤矿人员管理系统"

xadmin.site.register(views.CommAdminView,GlobalSetting)