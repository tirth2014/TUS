import xlrd, xlwt
from xlwt import Workbook

import xlsxwriter

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

            if len(cust_lst) >= 1:
                for cust in cust_lst:
                    if cust.get('C_Name') == cn_var:
                        total = cust.get('Total') + tot_var
                        tax = cust.get('Tax') + tax_var

                        cust.update({
                            'Total': total,
                            'Tax': tax
                        })
                        cust_update = True

            if not cust_update:
                cust_lst.append({
                    'C_Name': cn_var,
                    'Total': tot_var,
                    'Tax': tax_var
                })

for i in cust_lst:
    print(i)

cols = ['Customer Name', 'Total', 'Tax Amount']
filename = 'cust-order-xls-write.xls'

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
back_color = xlwt.easyxf('font: bold 1, color red;\
                        border: top_color black, bottom_color black, right_color black, left_color black;\
                       pattern: pattern solid, fore_colour yellow;')  # XFstyle
red_bold = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')

# back_color = xlwt.XFStyle()
# pattern = xlwt.Pattern()
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']
# back_color.pattern = pattern


blue_bold = xlwt.easyxf('font: bold 1, color blue;')
sheet1.write(0, 0, "Cust_Name", back_color)
sheet1.write(0, 1, "Total", back_color)
sheet1.write(0, 2, "Tax", back_color)
sheet1.col(0).width = 8000
sheet1.col(1).width = 4000
sheet1.col(2).width = 4000
grand_total = 0
grand_tax = 0
for i in range(len(cust_lst)):
    sheet1.write(i + 1, 0, cust_lst[i].get("C_Name"))
    sheet1.write(i + 1, 1, cust_lst[i].get("Total"))
    sheet1.write(i + 1, 2, cust_lst[i].get("Tax"))
    grand_total += cust_lst[i].get("Total")
    grand_tax += cust_lst[i].get("Tax")
sheet1.write((len(cust_lst)) + 1, 0, "GRAND TOTAL", red_bold)
sheet1.write((len(cust_lst)) + 1, 1, xlwt.Formula('B2+B14'), blue_bold)
sheet1.write((len(cust_lst)) + 1, 2, xlwt.Formula('C2+C14'), blue_bold)

font = xlwt.Font()
font.name = "Times New Roman"
font.height = 350
font.bold = True
# font.colour_index=00FF00
font_large = xlwt.XFStyle()
font_large.font = font
sheet1.write_merge(16, 17, 4, 6, 'Thank You!', font_large)

wb.save('xlwt-cust-data-tirth.xls')

# newFile = "/home/tirth/pythonProject/xlwt-cust-data-tirth.xls"

# wb1 = openpyxl.load_workbook(filename = newFile)
# wb1 = xlrd.open_workbook_xls(newFile)
# # worksheet = wb1.active
# worksheet = wb1.sheet_by_index(0)
#
# for col in worksheet.col:
#     max_len =0
#     column = col[0].column_letter
#     for cell in col:
#         try:
#             if len(str(cell.value)) > max_len:
#                 max_len = len(str(cell.value))
#         except:
#             pass
#     adjusted_width = (max_len+2)*1.2
#     worksheet.columns_dimensions[column].width = adjusted_width
