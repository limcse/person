#import requests
import io 
import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#url ='https://www.bilibili.com/video/av78398109?from=search&seid=5790108257816743723'

#resp =requests.get(url)

#print(resp.content.decode())
#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","work.settings")
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
import django
import xlrd
import datetime
if django.VERSION >= (1, 7):#自动判断版本
	django.setup()
def main():
	from login.models import User
	from datetime import date
	wb = xlrd.open_workbook('login/2.xls',encoding_override='utf-8')
	sheet = wb.sheet_by_index(0)
	tab = wb.sheet_by_name('Sheet1')
	cols = sheet.ncols
	rows = sheet.nrows
	print(rows)
	i=0
	for r in range(0,rows):
		i+=1
		card = tab.cell(r,0).value
		print (card)
		name = tab.row(r)[1].value
		print(name)
		unit = tab.cell(r,2).value
		print(unit)
		job_name = tab.cell(r,3).value
		level = tab.cell(r,4).value
		kind = tab.cell(r,5).value
		education = tab.cell(r,6).value
		if tab.cell(r,7).ctype == 3:
			date_tuple = xlrd.xldate_as_tuple(tab.cell(r,7).value,wb.datemode)
			birthday = datetime.date(*date_tuple[:3])
			blood = tab.cell(r,8).value
			identity = tab.cell(r,9).value
			address = tab.cell(r,10).value
			gh = tab.cell(r,11).value
			marriage = tab.cell(r,12).value
			phone = tab.cell(r,13).value
		if tab.cell(r,14).ctype == 3:
			date_tuple = xlrd.xldate_as_tuple(tab.cell(r,14).value,wb.datemode)
			job_time = datetime.date(*date_tuple[:3])
			native = tab.cell(r,15).value
			content = tab.cell(r,16).value
		User.objects.get_or_create(card=card,name=name,unit=unit,job_name=job_name,level=level,kind=kind,education=education,birthday=birthday,blood=blood,identity=identity,address=address,gh=gh,marriage=marriage,phone=phone,job_time=job_time,native=native,content=content)
		print(i)
if __name__ == "__main__":
	main()
	print('Done!')