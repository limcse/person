import xlrd
import sqlite3
import csv
from datetime import date
#from django.db import models

wb = xlrd.open_workbook('1.xls')#打开excel文件

sheets = wb.sheet_names() #获取excel的表名

print("excel对象",wb)

print("excel所有表名称",wb.sheet_names())

print("索引获取对象",wb.sheet_by_index(0))

print("索引获取对象",wb.sheets()[0])

tab = wb.sheet_by_name('Sheet1')

print("标签行数",tab.nrows)

print("标签列数",tab.ncols)

print("指定行内容",tab.row_values(0))

print("指定行内容索引第一行，从第四列",tab.row_values(0,3))

print("指定列内容",tab.col_values(0))#索引第一列数据

print("指定列内容",tab.col_values(0,5))#索引第一列数据，从第5行数据开始

print("通过行号索引：",tab.row(0)[1].value)#索引第1行第2列内容


dbPath = "d:/django/work/db.sqlite3"
print(dbPath)
con = sqlite3.connect(dbPath)
cur = con.cursor()
#读取excel表的数据
workbook = xlrd.open_workbook('1.xls')
#选取需要读取数据的那一页
sheet = workbook.sheet_by_index(0)
#获得行数和列数
rows =sheet.nrows
print (rows)
cols =sheet.ncols
import datetime
print(sheet)
for r in range(1,rows):
	dic = {}
	card = tab.cell(r,0).value
	name = tab.cell(r,1).value
	unit = tab.cell(r,2).value
	job_name = tab.cell(r,3).value
	if tab.cell(r,7).ctype == 3:
		date_tuple = xlrd.xldate_as_tuple(tab.cell(r,7).value, workbook.datemode)
		x = datetime.date(*date_tuple[:3])
		print(x)
	if tab.cell(r,14).ctype == 3:
		date_tuple = xlrd.xldate_as_tuple(tab.cell(r,14).value, workbook.datemode)
		y = datetime.date(*date_tuple[:3])
		print(y)


		

con.commit()
cur.close()
con.close()
