a=int(input("a giriniz:"))
b=int(input("b giriniz:"))
c=int(input("c giriniz:"))

def toplama(a,b,c): #Birinci Fonksiyon
    return a+b+c # Hatalı Hali --> print("Toplamları",a+b+c)

def ikiylecarp(a): #İkinci Fonksiyon
    return a*2 # Hatalı Hali --> print("2 ile çarpılmış hali",a*2)

toplam=toplama(a,b,c)

print(ikiylecarp(toplam))