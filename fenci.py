import fool
import xlrd
import xlwt

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')

data = xlrd.open_workbook('zwcg.xls')

table = data.sheet_by_name(u'Sheet1')
nrows = table.nrows

for i in range(nrows):
	text = table.row_values(i)
	worklist = fool.cut(text[0])
	for j in range(len(worklist)):
		worksheet.write(i,j,label=worklist[j])

workbook.save('result.xls')

