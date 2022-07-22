import xlrd

filename = 'sample.xls'

loc = '/home/tirth/Downloads/saple.xls'

wb = xlrd.open_workbook_xls(loc)
sheet = wb.sheet_by_index(0)
# sheet.cell_value(1,1)

for i in range(sheet.nrows):
    print(sheet.cell_value(i,2))

