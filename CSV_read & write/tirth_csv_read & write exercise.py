import csv

customer = []
dic = {}

with open("sales_order_sheet_read_csv.csv", 'r') as file:

    csvF = csv.DictReader(file)
    for i in csvF:
        # if i['Total'] != '':
        if i['Status'] == 'Sales Order':
            ord_ref_lst = []
            total = float(i['Total'])
            untaxed = float(i['Untaxed Amount'])
            tax = total - untaxed
            ord_ref = i['Order Reference']
            ord_perc = tax * 100 / total
            cust_name = i['Customer']
            perc_dic = {}
            cust_update = False

            if len(customer) >= 1:
                for cust in customer:

                    if cust.get('c_name') == cust_name:
                        ord_ref_lst = cust.get('Ord_ref')
                        ord_ref_lst.append(ord_ref)
                        tot = cust.get('Total') + total
                        tax_amt = cust.get('Tax') + tax
                        perc_dic = cust.get('Tax Percent')
                        perc_dic[ord_ref] = ord_perc
                        cust.update({
                            'Total': tot,
                            'Tax': tax_amt,
                            'Ord_ref': ord_ref_lst,
                            'Tax Percent': perc_dic
                        })
                        cust_update = True

            if not cust_update:
                ord_ref_lst.append(ord_ref)
                perc_dic[ord_ref] = ord_perc
                customer.append({
                    'c_name': cust_name,
                    'Total': total,
                    'Tax': tax,
                    'Ord_ref': ord_ref_lst,
                    'Tax Percent': perc_dic
                })
    for i in customer:
        print(i)

cols = ['Customer Name','Total','Tax Amount','Ref. No', 'Tax_Percentage']
filename = 'customer-order-datae.csv'

with open(filename,'w') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(cols)
    name = ''

    for i in customer:
        for j,k in zip(i.get('Ord_ref'),(i.get('Tax Percent')).values()):
            if name != i.get('c_name'):
                csvwriter.writerow([i.get('c_name'),i.get('Total'),i.get('Tax'), j,k])
                name = i.get('c_name')
            else:
                csvwriter.writerow(['', '', '', j, k])

# with open("customer-order-datae.csv", 'r') as nfile:
#
#     csvF_n = csv.DictReader(nfile)
#     for i in csvF_n:
#         print(i)
