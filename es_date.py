import datetime
#1
y = datetime.datetime.now()
print(y)
#2
x = datetime.datetime(2006, 5, 24)
print(x)
#3
print(x.strftime("%m"))
#4
print(x.strftime("%A"), x.strftime("%d"), x.strftime("%m"), x.strftime("%Y"))
#5
a = y-x
print(a.days,"giorni")