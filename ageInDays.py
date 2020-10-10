import datetime

def days_in_month(year, month):
    # Returns:
    #   The number of days in the input month.
    if month==12:
        return 31
    else:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month+1, 1)
        diff = date2 - date1
        return(diff.days) 

def is_valid_date(year, month, day):
    # Returns:
    #   True if year-month-day is a valid date and
    #   False otherwise
    if (datetime.MINYEAR<=year<=datetime.MAXYEAR) and (1<=month<=12) and (1<=day<= days_in_month(year, month)):
        return True
    else:
        return False

day=int(input("Enter your Birth date : "))
month=int(input("Enter your Birth month : "))
year=int(input("Enter your Birth year : "))

if is_valid_date(year,month,day):
    given = datetime.date(year,month,day)
    today = datetime.date.today()
    res = today - given
    given_date = str(day)+'/'+str(month)+'/'+str(year)
    print(given_date+" in days is : ",res.days,"days")
else:
    print("Invalid Date")