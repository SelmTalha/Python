vize=int(input("Vize notunu giriniz:"))
vize2=int(input("Vize notunu giriniz:"))
final=int(input("Vize notunu giriniz:"))

toplam=(vize*30/100)+(vize2*30/100)+(final*40/100)

if(toplam>=90):
    print("AA")
elif(toplam>=85):
    print("BA")
elif(toplam>=80):
    print("BB")
elif(toplam>=75):
    print("CB")
elif(toplam>=70):
    print("CC")
elif(toplam>=65):
    print("DC")
elif(toplam>=60):
    print("DD")
elif(toplam>=55):
    print("FD")
else:
    print("FF")