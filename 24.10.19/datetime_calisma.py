from datetime import datetime #*
#KAYNAK : w3schools.com

#print(dir(datetime))

print(datetime.now())

dt=datetime.now()

print(dt.year) #Yıl
print(dt.month) #Ay
print(dt.day) #Gün
print(dt.hour) #Saat
print(dt.minute) #Dakika
print(dt.second) #Saniye

print(datetime.ctime(dt))

print(datetime.strftime(dt,'%Y'))
print(datetime.strftime(dt,'%X'))
print(datetime.strftime(dt,'%d'))
print(datetime.strftime(dt,'%A'))
print(datetime.strftime(dt,'%B'))

print(datetime.strftime(dt,'%Y %B %A'))

t='15 April 2019 10:12:30'

result=datetime.strptime(t,'%d %B %Y %H:%M:%S')

print(result)

birthday=datetime(1999,5,19,12,26,00)
print(birthday)
