from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pencere.ui',self)
        self.game_board_olustur(4)
        print(self.random_sayilar_al(4))
        self.shuffle_board_olustur(4)
    
    def game_board_olustur(self,n):
        x=0
        y=0
        for i in range((n ** 2)+1):
            btn=QPushButton()
            btn.setText("")
            btn.setObjectName(str(i))
            self.gl_game_board.addWidget(btn,y,x,1,1)
            x+=1
            if i % n ==0 and i!=0:
                y+=1
            if i % n ==0:
                x=0

    def random_sayilar_al(self,n):
        import random
        temp=[i for i in range(n**2)]
        karisik=[]
        for x in range(n**2):
            rnd=random.randint(0,len(temp)-1)
            rnd_value=int(temp[rnd])
            karisik.append(rnd_value)
            temp.remove(rnd_value)
        return karisik

    def shuffle_board_olustur(self,n):
        rastgele_Sayilar=self.random_sayilar_al(n)
        x=0
        y=0
        for i in range(n):
            for j in range(n):
                btn=QPushButton()
                btn.setText("")
                btn.setObjectName(str(rastgele_Sayilar.pop()))
                self.gl_shuffle_board.addWidget(btn,i,j,1,1)
                

        
        #board'a buton eklemeye yarıyor -->
        #btn=QPushButton()
        #btn.setText('asd')
        #self.gl_game_board.addWidget(btn,0,0,1,1)
        #btn2=QPushButton()
        #btn2.setText('btn2')
        #self.gl_game_board.addWidget(btn2,1,1,1,1)

app=QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())