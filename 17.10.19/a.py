import random

value=random.random()
value=random.uniform(1,20)
value=random.randint(1,20)

print(value)

#Choice = Liste içinden rastgele eleman seçiyo her defasında değiştiriyor.Kura çekilişi mantığı !
names= ["elif","gözde","yasemin","selim"]
result=random.choice(names)
result=random.sample(names,2) #Sample: Rastgele çekilişe değer girerek adedi artırıyor.2 yazarsak 2 isim gözükür gibi. 
print(result)



