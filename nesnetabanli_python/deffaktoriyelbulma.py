sayi=int(input("Sayiyi giriniz :"))

def fakt():
	faktoriyel=1
	for i in range(sayi):
		faktoriyel=faktoriyel*(i+1)
	return faktoriyel
print(fakt())
