from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=5))

now = datetime.now()
print("Today's date: "+ str(now))

print("One Year from now: " + str(now+timedelta(days=365)))
print("Two Days and 3 Weeks from now: " + str(now+timedelta(days=2, weeks=3)))

t = datetime.now() - timedelta(weeks=1)
s= t.strftime("%A %B %d %Y")
print("One week ago it was " + str(s))
today = date.today()
afd = date(today.year, 4, 1)
if afd<today:
    print("April Fool's day was %d days ago "%((today-afd).days))
    afd = afd.replace(year=today.year+1)

time_to_afd = afd - today
print("Its just ", time_to_afd.days, " days left for next year April Fool's day")