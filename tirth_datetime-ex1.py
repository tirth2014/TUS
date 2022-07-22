# Parse the following date strings to datetime format (easy)
#
# Input
s1 = "2010 Jan 1"
s2 = '31-1-2000'
s3 = 'October10, 1996, 10:40pm'

from datetime import datetime
from dateutil import parser

d1 = parser.parse(s1)
d2 = parser.parse(s2)
d3 = parser.parse(s3)

d11 = datetime.strptime(s1,'%Y %b %d').strftime('%Y-%m-%d %H:%M:%S')
d22 = datetime.strptime(s2,'%d-%m-%Y').strftime('%Y-%m-%d %H:%M:%S')
d33 = datetime.strptime(s3,'%B%d, %Y, %H:%M%p').strftime('%Y-%m-%d %H:%M:%S')

print(d1)
print(d2)
print(d3)

print(d11)
print(d22)
print(d33)