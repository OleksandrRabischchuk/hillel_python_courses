import datetime
my_date = datetime.datetime.now()
my_year = lambda x: x.year
my_month = lambda x: x.month
my_day = lambda x: x.day
print(my_year(my_date))
print(my_month(my_date))
print(my_day((my_date)))