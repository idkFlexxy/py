import datetime
today=datetime.datetime.now().date()
print("current date is :", today)
dta=int(input("enter the number of days to add:"))
newdate=today +datetime.timedelta(days=dta)

print("date after adding",dta,"day is",newdate)
