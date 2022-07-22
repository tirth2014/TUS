import xlrd, xlwt, xlsxwriter
from xlwt import Workbook

loc = "/home/tirth/pythonProject/sales_order_sheet_read_csv.xls"

wb = xlrd.open_workbook_xls(loc)
sheet = wb.sheet_by_index(0)
cust_lst = []

for i in range(1, sheet.nrows):
    if sheet.cell_value(i, 4) == 'Sales Order':
        cn_var = sheet.cell_value(i, 2)
        cust_update = False
        if cn_var != '':
            tot_var = float(sheet.cell_value(i, 10))
            untax_var = float(sheet.cell_value(i, 11))
            tax_var = tot_var - untax_var
            cust_update = False
            if len(cust_lst) >= 1:
                for cust in cust_lst:
                    if cust.get('C_Name') == cn_var:
                        total_lst = cust.get('Total')
                        tax_lst = cust.get('Tax')
                        total_lst.append(tot_var)
                        tax_lst.append(tax_var)
                        cust.update({
                            'Total': total_lst,
                            'Tax': tax_lst
                        })
                        cust_update = True

            if not cust_update:
                cust_lst.append({
                    'C_Name': cn_var,
                    'Total': [tot_var],
                    'Tax': [tax_var],
                })

for i in cust_lst:
    print(i)

#   write the data
workbook = xlsxwriter.Workbook('tirth_cust-xlsx.xlsx')
worksheet = workbook.add_worksheet()

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'yellow'
})

item_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter'
})

head_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'
})
worksheet.merge_range('A1:O1', 'Customer Data', merge_format)
worksheet.write(1, 0, 'Cust_Name: ', head_format)
worksheet.write(2, 0, 'Total: ', head_format)
worksheet.write(3, 0, 'Tax: ', head_format)

row, col = 0, 0
c = 1
for i in range(len(cust_lst)):
    worksheet.write(1, i + 1, cust_lst[i].get('C_Name'))
    tot = 0
    tax = 0
    for j in cust_lst[i].get('Total'):
        tot += j
        worksheet.write(2, c, tot, item_format)
    for j in cust_lst[i].get('Tax'):
        tax += j
        worksheet.write(3, c, tax, item_format)
    c += 1
worksheet.write(2, c, '=SUM(B3:N3)')
worksheet.write(3, c, '=SUM(B4:N4)')
worksheet.set_column(0, len(cust_lst), 15)

workbook.close()



