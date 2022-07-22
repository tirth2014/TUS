from datetime import datetime, timedelta, date
import pytz, calendar
from dateutil.tz import *

d = date(2022, 6, 3)
print(type(d))
tdy = date.today()
ystrdy = date.today() - timedelta(1)
tmrw = date.today() + timedelta(1)
print(d)
print("Today's date is: %s" % tdy)
print("Yesterday's date is: %s" % ystrdy)
print("Tomorrow's date is: %s" % tmrw)
print("today's day in no. is: %s" % tdy.weekday())
print("today's day is: %s" % tdy.strftime('%A'))
print("yesterday's day is: %s" % ystrdy.strftime('%a'))
print("date after 7 days is: ", tdy+timedelta(days=7))
print("today's date in another format is: {:%d, %B, %Y}".format(tdy))
print("today's date in another format is: {:%d/%m/%Y}".format(tdy))
print(f"today's datetime:  {datetime.now(): %d-%m-%Y and time is %H hrs %M minutes}")
print("today's date: ", tdy.strftime('%d - %m - %Y'))

bdy = date(2023, 12, 20)
till_bdy = bdy - tdy
print("np. of days till birthday are: ",till_bdy.days)

dttym = datetime(2020, 12, 20, 4, 45, 58,10000)
print("time on the date is: ", dttym.time())
print("date given is: {:%d/%m/%Y}".format(dttym.date()))
print(dttym.year)
indtym = datetime.now(pytz.timezone('Asia/Kolkata'))
grmnytym = datetime.now(pytz.timezone('Europe/Berlin'))
rustym = datetime.now(pytz.timezone('Europe/Moscow'))
print("time in india is: ", indtym)
print("time in germany is: ", grmnytym)
print("time in russia is: ", rustym)
now = datetime.now()
utc= tzutc()
now = now.replace(tzinfo=utc)
utc_now = now.astimezone(utc)
print(utc_now)

tz = pytz.timezone('Europe/Berlin')
germany_now = now.astimezone(tz)
print(germany_now)

for tz in pytz.all_timezones:
    print(tz)
# weekday:  monday - 0  and sunday - 6
# isoweekday:  monday - 1  and sunday - 7
