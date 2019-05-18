sayi1 = float(input("Birinci Sayıyı Giriniz : "))
sayi2 = float(input("İkinci Sayıyı Giriniz : "))
print("1.Toplama İşlemi")
print("2.Çıkarma İşlemi")
print("3.Çarpma İşlemi")
print("4.Bölme İşlemi")
secim=int(input("Lütfen islemi seciniz ?:"))

if(secim>0 and secim<5):
    if(secim==1):
        print(sayi1+sayi2)
    if(secim==2):
        print(sayi1-sayi2)
    if(secim==3):
        print(sayi1*sayi2)
    if(secim==4):
        print(sayi1/sayi2)
else:
    print("Yanlıs secim yaptiniz !")
