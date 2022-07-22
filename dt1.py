# How do I get the day of week given a date?

from _datetime import datetime,date
import calendar

my_date = datetime(int(input("enter year")),int(input("enter month")),int(input("enter day")))
print(my_date.strftime('%A'))

# count number of any weekdays between two dates:

d1 = date(int(input("enter year")),int(input("enter month")),int(input("enter day")))
d2 = date(int(input("enter year")),int(input("enter month")),int(input("enter day")))

count = 0

for d_ord in range(d1.toordinal(), d2.toordinal()):
    d = date.fromordinal(d_ord)
    if d.weekday() == int(input("enter weekday number: ")):
        count += 1

print("The number of weekdays between two dates are: ", count)



