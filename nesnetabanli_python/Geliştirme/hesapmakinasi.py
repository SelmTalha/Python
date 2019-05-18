a=int(input("1.Sayi giriniz:"))
b=int(input("2.Sayi giriniz:"))

def toplamafonk():
    return a+b

def cikarmafonk():
    return a-b

def carpmafonk():
    return a*b

def bolmefonk():
    return float(a)/float(b)
print("Lütfen yapacağınız işlemi seçiniz :")
print("1.Toplama İşlemi")
print("2.Çıkarma İşlemi")
print("3.Çarpma İşlemi")
print("4.Bölme İşlemi")

c=int(input("Seçim yapiniz:"))

if(c==1):
    print("Toplama İşlemi Sonucu :",toplamafonk())
elif(c==2):
    print("Çıkarma İşlemi Sonucu :",cikarmafonk())
elif(c==3):
    print("Çarpma İşlemi Sonucu :",carpmafonk())
elif(c==4):
    print("Bölme İşlemi Sonucu :",bolmefonk())
else:
    print("İşlem hatası !")