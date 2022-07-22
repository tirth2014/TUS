import csv

# with open("democsv-file.csv", newline="") as file:
#     csvFile = csv.DictReader(file)
#
#     for i in csvFile:
#         print(i)

f = open("democsv-file.csv", "r")
f2 = csv.DictReader(f)
for i in f2:
    print(i)

# print('%d'%f2.line_num)
#
# for x
