import csv

#
# with open("democsv-file.csv") as demo:
#     with open("heycsv.csv", 'w') as csvfile:
#         reader = csv.DictReader(demo, delimiter = ',')
#         writer = csv.DictWriter(csvfile, reader.fieldnames, delimiter = '|')
#         writer.writeheader()
#         writer.writerows(reader)

# import csv
# with open('eggs.csv', 'a', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='#', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

readF = open("eggs.csv", 'r')
f = csv.DictReader(readF)
for i in f:
    print(i)

dic = {"name":"tirth", "age": 21}



