
#Kalıtım (İnheritance)
#Class Örnekleri ve işlemler 
#Örnek Soru Çözümleri 

class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara #yazılımcı objelerinin özellikleri
        self.maas=maas
        self.diller=diller

    def bilgileri_goster(self):
        print("""
        Çalışan Bilgisi:

        İsim: {}

        Soyisim: {}

        Şirket Numarası: {}

        Maaş: {}

        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)

    def maas_yukselt(self,zam_miktari):
        print("Maaş yükseliyor...")
        self.maas+= 250

yazilimci1=Yazılımcı("Selim Talha","Çağlar","36","2500",["Python","Java","C"])
yazilimci2=Yazılımcı("Beyza","Çağlar","24","1900",["PHP","JS","CSS","HTML"])

yazilimci1.dil_ekle("Unity")

yazilimci1.bilgileri_goster()

