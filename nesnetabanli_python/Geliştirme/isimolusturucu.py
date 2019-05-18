#Dizideki isim ve soyisimleri karışık olarak ekrana getirme işlemini yap !
#01 İsim Oluşturma !

import random

def rastgele_isim_soyisim():
    ad =["Selim","Elif","Gözde","Yasemin","Habibe","Yasin","Yaren","Fulya","Orhan"]
    soyad =["Çağlar","Bayram","Akman","İnce","Gültekin","Türkandlı","Ertok","Babacan","Geyek"]
    return "{} {}".format(random.choice(ad),random.choice(soyad))
for i in range(5):
    print(rastgele_isim_soyisim())

#Choice = Seçim demektir .
#choice=="2" gibi bir ifade seçim 2 olursa demektir.Menü özelliği olarak kullanılabilir. !
