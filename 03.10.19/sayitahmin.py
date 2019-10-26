import random

randomsayi=random.randint(1,100)

while(True):
    a=int(input("Bir sayi giriniz:"))
    if (a>0 and a<100):
        if (a<randomsayi):
            print("Daha büyük")
        elif(a>randomsayi):
            print("Daha küçük")
        else:
            print("Doğru bildiniz !")
            break
    else:
        print("Fazla yada az değer girdiniz 1-100 arası bir değer giriniz.")