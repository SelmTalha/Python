class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri....")
        print("İsim:{} \nMaas:{} \nDepartman:{} ".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor...")
        self.departman=yeni_departman
    
class Yönetici(Çalışan):
    pass 

yonetici1=Yönetici("Mehmet Baltacı",3000,"İnsan Kaynakları")
#Çalışan sınıfının init fonksiyonu
yonetici1.bilgileri_goster()
#print(dir(yonetici1))
yonetici1.departman_degistir("Halkla İlişkiler")
yonetici1.bilgileri_goster()