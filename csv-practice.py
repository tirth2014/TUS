import csv

cols = ['name','en.no','city']

rows = [['tirth','21','ahmedabad'],
        ['milan','21','junagadh'],
        ['manav','22','modasa']
        ]

with open("democsv-file.csv",'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(cols)
    csvwriter.writerows(rows)
lst = []
for i in range(4):
    lst

