a=int(input("Sayiyi giriniz:"))

def asalsayibul(a): 
    for i in range(2,a):
        if(a%i==0):
            print("Asal Değil")
            break
    else:
        print("Asal Sayı")


asalsayibul(a)

#15,49,81
