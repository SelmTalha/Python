class Araba():
    def __init__(self,model,renk,beygir_gücü,silindir):
        self.model=model
        self.renk=renk
        self.beygir_gücü=beygir_gücü
        self.silindir=silindir
araba1=Araba("Peugeot 301","Gümüş",110,4)
araba2=Araba("Renault Megane","Siyah",105,4)
print("Araba1 model = "+araba1.model)
print("Araba2 renk = "+araba2.renk)