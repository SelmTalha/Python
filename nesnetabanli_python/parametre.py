def toplama(*parametreler):#Artık parametreler değişken
    toplam=0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam+=i
    return toplam
print(toplama(3,4,5,6,7,8,9,10))