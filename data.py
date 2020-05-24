import datetime

data=datetime.datetime.now()
print(f"{data.day}/{data.month}/{data.year}")

nasc=datetime.datetime(1989,3,22)
print(nasc.strftime("%A"))

print(nasc.strftime("%a"))
print(nasc.strftime("%w"))
print(nasc.strftime("%d"))
print(nasc.strftime("%b"))
print(nasc.strftime("%B"))
print(nasc.strftime("%m"))
print(nasc.strftime("%Y"))
print(nasc.strftime("%y"))

#Hours

print(nasc.strftime("%H"))
print(nasc.strftime("%I"))
print(nasc.strftime("%p"))
print(nasc.strftime("%M"))
print(data.strftime("%f"))
print(nasc.strftime("%j"))
print(nasc.strftime("%W"))
