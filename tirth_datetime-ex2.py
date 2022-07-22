#How many days has it been since you were born? (easy)
# Input
bday = 'Oct 2, 1869'  # use bday

from dateutil import parser

from datetime import datetime,date
bday = parser.parse(bday)
tdy = date.today()
print("np. of days till birthday are: ",(tdy-bday.date()).days)

