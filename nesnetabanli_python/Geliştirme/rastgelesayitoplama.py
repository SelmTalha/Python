import random

a=random.randint(1,50)
b=random.randint(1,50)

print(a,"+",b)
c=int(input("Sonucu giriniz:"))

def toplamafonk():
    return a+b

if(c==toplamafonk()):
    print("Sonucunuz Doğru !")
else:
    print("Sonuç yanlış!")