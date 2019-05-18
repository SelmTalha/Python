print("I   --> [Toplama Islemi]")
print("II  --> [Cikarma Islemi]")
print("III --> [Carpma Islemi]" )
print("IV  --> [Bolme Islemi]"  )

islem=int(input("Seciminizi yapiniz :"))

sayi1=int(input("1.Sayiyi giriniz :"  ))
sayi2=int(input("2.Sayiyi giriniz :"  ))

def toplamfefafonk(sayi1,sayi2):
	return sayi1+sayi2

def cikarmafonk(sayi1,sayi2):
	return sayi1-sayi2

def carpmafonk(sayi1,sayi2):
	return sayi1*sayi2

def bolmefonk(sayi1,sayi2):
	return float(sayi1)/float(sayi2)

if (islem==1):
	print(toplamafonk(sayi1,sayi2))
elif (islem==2):
	print(cikarmafonk(sayi1,sayi2))
elif (islem==3):
	print(carpmafonk(sayi1,sayi2))
elif (islem==4):
	print(bolmefonk(sayi1,sayi2))
else:
	print("Hatali islem yaptiniz!")
