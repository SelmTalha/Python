a=input("Sayi giriniz:")
kuvvet=len(a)
a=int(a)
r=0
toplam=0
kontrol=a
for i in range(kuvvet):
    r=a%10
    toplam+=r**kuvvet
    a=a/10
if(toplam=kontrol):
    print("Armstrong Sayısıdır.")
else:
    print("Değildir.")