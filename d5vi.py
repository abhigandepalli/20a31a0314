import datetime
base=datetime.datetime.today()
for x in range (0,10):
    print(base+datetime.timedelta(days=x))
