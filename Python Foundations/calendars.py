import calendar

#text calendar
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2017, 1,0,0)
print(st)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#HTML Calendar

for i in c.itermonthdays(2017,8):
    print(i)
ht = calendar.HTMLCalendar(calendar.MONDAY)
x = ht.formatmonth(2017,1)
print(x)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for month in calendar.month_name:
    print(month)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for day in calendar.day_name:
    print(day)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#Calculate Days based on Rules
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Team Meetings will be on - ")

for m in range(1,13):
    cal = calendar.monthcalendar(2022,m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
    print("%10s %2d" %(calendar.month_name[m], meetday))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
