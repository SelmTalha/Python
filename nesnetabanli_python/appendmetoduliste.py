#liste'den liste2'yi oluşturalım.

liste1 = [1,2,3,4,5]

liste2 = list() #veya liste2=[] ikiside boş liste oluşturur.

for i in liste1:
    liste2.append(i) #liste2'ye liste1'in elemanlarını ekledik.

print(liste2)