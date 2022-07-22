# Count the number of saturdays between two dates (medium)

# Input
from datetime import datetime, date
from datetime import timedelta

d1 = date(1869, 1, 2)
d2 = date(2020, 10, 2)
count = 0# Count the number of saturdays between two dates (medium)

# Input
from datetime import datetime, date
from datetime import timedelta

d1 = date(1869, 1, 2)
d2 = date(2020, 10, 2)
count = 0
#
# for d_ord in range(d1.toordinal(), d2.toordinal()):
#     d = date.fromordinal(d_ord)
#     if d.weekday() == 5:
#         count += 1
#
# print("The number of saturdays between two dates are: ", count)

days = (d2 - d1).days

for i in range(days):
    if d1.strftime('%a') == "Sat":
        count += 1
    d1 += timedelta(days=1)

print("The number of saturdays between two dates are: ", count)
# Desired Output
# > 40

#
# for d_ord in range(d1.toordinal(), d2.toordinal()):
#     d = date.fromordinal(d_ord)
#     if d.weekday() == 5:
#         count += 1
#
# print("The number of saturdays between two dates are: ", count)

days = (d2 - d1).days

for i in range(days):
    if d1.strftime('%a') == "Sat":
        count += 1
    d1 += timedelta(days=1)

print("The number of saturdays between two dates are: ", count)
# Desired Output
# > 40
