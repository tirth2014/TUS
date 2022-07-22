import xlsxwriter

workbook = xlsxwriter.Workbook('expenses01.xlsx')
worksheet = workbook.add_worksheet()

expenses = (
    ['Rent', 8000],
    ['Food', 2000],
    ['Electricity', 1000],
    ['Fuel', 2000]
)

row = 0
col = 0
worksheet.write(row, col, "ITEM")
worksheet.write(row, col + 1, "COST")
for item, cost in expenses:
    worksheet.write(row + 1, col, item)
    worksheet.write(row + 1, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B2:B4)')

workbook.close()
