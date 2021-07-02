from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Todays date is - " , today.day)
    print("Todays month is - " , today.month)
    print("Todays year is - " , today.year)
    print("Todays weekday is - " , today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a : ", days[today.weekday()])
    time_and_date = datetime.now()
    print("Today's date and time is - ", time_and_date)
    t = datetime.time(datetime.now())
    print(t)
    

if __name__ == "__main__":
    main()