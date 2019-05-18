#3'e ve 5'e tam bölünen sayıları bulma fonksiyonla!

def fonk():
    for i in range(1,100,1):
        if(i%3==0 and i%5==0):
            print(i)
fonk()