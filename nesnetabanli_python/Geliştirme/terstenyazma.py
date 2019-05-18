isim=input("İsminizi giriniz:")

print(isim[::-1])

print("-------")

for i in range(len(isim)-1,-1,-1):
    print(isim[i])