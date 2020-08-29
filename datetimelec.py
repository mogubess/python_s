import datetime


now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

print(datetime.date.today())

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)

