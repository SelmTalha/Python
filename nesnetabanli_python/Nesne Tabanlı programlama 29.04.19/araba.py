#Class içinde verdiğimiz değerler her oluşturduğumuz objeye işlenir.
#araba2.py örneğinde ise parametre ile init fonksiyonu içerisinde ; parametre ile obje içeriklerini elle girmemiz sağlandı !
class Araba():
    model="Renault Megane"
    renk="Gümüş"
    beygir_gücü=110
    silindir=4
    def __init__(self):
        print("init fonksiyonu çağrıldı.")


araba1=Araba()
print(araba1.model)
araba1.beygir_gücü=120
print(araba1.beygir_gücü)
print(dir(araba1))

