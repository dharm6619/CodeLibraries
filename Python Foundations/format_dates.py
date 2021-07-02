from datetime import datetime

now = datetime.now()
print(now.strftime("THE CURRENT YEAR - %y"))
print(now.strftime(" Locale Date- %x"))
print(now.strftime(" Locale Time- %X"))
print(now.strftime(" %a, %M, %d, %Y, %x"))
