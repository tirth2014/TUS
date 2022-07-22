import csv

cust = []
total = {}
tax = {}
tax_percent = {}
tax_perc = {}

with open("sales_order_sheet_read_csv.csv", 'r') as file:
    csvF = csv.DictReader(file)
    for i in csvF:
        if i['Status'] == 'Sales Order':
            print(i)

        if i['Customer'] not in total.keys() and i['Total'] != '':
            total[i['Customer']] = float(i['Total'])

        elif i['Customer'] in total.keys() and i['Total'] != '':
            total[i['Customer']] += float(i['Total'])

        if i['Customer'] not in tax.keys() and i['Untaxed Amount'] != '':
            tax[i['Customer']] = float(i['Total']) - float(i['Untaxed Amount'])

        elif i['Customer'] in tax.keys() and i['Untaxed Amount'] != '':
            tax[i['Customer']] += float(i['Total']) - float(i['Untaxed Amount'])

        if i['Order Reference'] != '':
            tax_perc[i['Order Reference']] = (float(i['Total']) - float(i['Untaxed Amount'])) * 100 / float(i['Total'])

    for i in total.keys():
        tax_percent[i] = tax[i] * 100 / total[i]


    print("\n\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("Total order amount is: ", total)
    print("-------------------------------------------------------------------------------------------------------------")
    print("Total Tax is: ", tax)
    print("-------------------------------------------------------------------------------------------------------------")
    print("Tax percent is: ", tax_percent)
    print("-------------------------------------------------------------------------------------------------------------")
    print("tax % is: ", tax_perc)

