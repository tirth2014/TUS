import xlrd, xlwt

import xlsxwriter

wb = xlsxwriter.Workbook('sample.xlsx')
worksheet = wb.add_worksheet()

worksheet.write('A1',"first cell")
worksheet.write('B1','1st row 2nd col')
worksheet.write('A2','under 1st cell')
worksheet.write_row()

wb.close()

# read

filename = 'sample.xlsx'
loc = '/home/tirth/pythonProject/sample.xlsx'


workbook = xlrd.open_workbook_xls(loc)
sht = workbook.sheet_by_index(0)

for i in range(sht.nrows):
    print(sht.cell_value(i,1))