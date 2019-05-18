class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara #yazılımcı objelerinin özellikleri
        self.maas=maas
        self.diller=diller
yazilimci1=Yazılımcı("Selim Talha","Çağlar","36","2500",["Python","Java","C"])
yazilimci2=Yazılımcı("Beyza","Çağlar","24","1900",["PHP","JS","CSS","HTML"])

print(yazilimci1.diller)




        